#!/home/jeffmur/archiconda3/envs/face_recon/bin/python3
from pathlib import Path
from datetime import datetime
import signal,sys,time
from google.cloud import pubsub_v1

# TODO(developer)
project_id = "smartmirror-fba08"
topic_id = "faceRecon"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)
minDelta = 3 # seconds between publish events

def publishStatus(isActive):

    if(isActive):
        print(f"[{datetime.now()}] -- Jeffrey Detected")
    else:
        print(f"[{datetime.now()}] -- Jeffrey Left")

    # Else publish event
    status = "ACTIVE" if isActive else "LEFT"
    data = f"Jeffrey-{status}" #, self.keyIter)
    # Data must be a bytestring
    data = data.encode("utf-8")
    # Add two attributes, origin and username, to the message

    publisher.publish(
        topic_path, data, update=status, user="Jeffrey"
    )

init = True
while True: 
    time.sleep(5.0)
    publishStatus(init)
    init = not init