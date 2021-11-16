#!/home/jeffmur/archiconda3/envs/face_recon/bin/python3
import face_recognition
import cv2
import numpy as np
import pickle
from pathlib import Path
from datetime import datetime
import signal,sys,time    
from google.cloud import pubsub_v1

# TODO (developer config)
project_id = "{GOOGLE_CLOUD_PROJECT_ID}"
topic_id = "{GOOGLE_PUB_SUB_ENDPOINT}"
# Images and Names
known_users = [User("Bob", "path/to/Bob.jpg"), User("Alice", "path/to/Alice.jpg")]
# end config 

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)
minDelta = 3 # seconds between publish events

class User: 
    # Initaliziation
    def __init__(self, name, picturePath):
        self.active = False
        self.name = name
        self.picture = picturePath
        self.postTime = datetime.now()

    def publishStatus(self):

        if(self.active):
            print(f"[{datetime.now()}] -- {self.name} Detected")
        else:
            print(f"[{datetime.now()}] -- {self.name} Left")

        # Else publish event
        status = "ACTIVE" if self.active else "LEFT"
        data = f"{self.name}-{status}" #, self.keyIter)
        # Data must be a bytestring
        data = data.encode("utf-8")
        # Add two attributes, origin and username, to the message

        publisher.publish(
            topic_path, data, update=status, user=str(self.name)
        )

    def updateStatus(self, isThere):
        # Only send data every {delta} seconds
        current_time = datetime.now()
        diff = current_time - self.postTime 
        
        total = diff.total_seconds()

        if(total <= minDelta): return

        self.postTime = current_time
        
        if(self.active != isThere):
            self.active = isThere 
            self.publishStatus()

    def newEncoding(self):
        p = Path(f"{self.name}_face.dat")
        if(not p.exists()):
            # Load a sample picture and learn how to recognize it.
            user_image = face_recognition.load_image_file(self.picture)
            try:
                user_face_encoding = face_recognition.face_encodings(user_image)[0]
            except IndexError as error: 
                raise "No Face Recognized, please supply a higher resolution image!"

            with open(f"{self.name}_face.dat", "wb") as face_data_file:
                pickle.dump(user_face_encoding, face_data_file)
                print(f"{self.name} face saved to disk.")
            
            return user_face_encoding
        else: 
            print(f"Loading {self.name} face from cache")
            self.loadEncoding()

    def loadEncoding(self):
        try:
            with open(f"{self.name}_face.dat", "rb") as face_data_file:
                user_face_encoding = pickle.load(face_data_file)
            print(f"Success! -- Loaded {self.name}")
            return user_face_encoding
        except FileNotFoundError as e:
            print("No previous face data found - saving a new face!")
            return self.newEncoding()


# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Create arrays of known face encodings and their names
known_face_encodings = [x.loadEncoding() for x in known_users]
known_face_names = [x.name for x in known_users]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Graceful exist                    
terminate = False                            

def signal_handling(signum,frame):           
    global terminate                         
    terminate = True                         

print("Ready")
while True:
    signal.signal(signal.SIGINT,signal_handling)
    if terminate:                       
        print('\n')     
        video_capture.release()  
        break                      

    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        # "Leaving" if face is not detected, set all status to false
        if(face_encodings == []):
            for user in known_users: 
                user.updateStatus(False)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            if(np.any(matches)):
                # Use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    for u in known_users: 
                        if(name == u.name): u.updateStatus(True)

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    # for (top, right, bottom, left), name in zip(face_locations, face_names):
    #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
    #     top *= 4
    #     right *= 4
    #     bottom *= 4
    #     left *= 4

    #     # Draw a box around the face
    #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    #     # Draw a label with a name below the face
    #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    #     font = cv2.FONT_HERSHEY_DUPLEX
    #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # # Display the resulting image
    # cv2.imshow('Video', frame)

    # # Hit 'q' on the keyboard to quit!
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release handle to the webcam
# cv2.destroyAllWindows()
