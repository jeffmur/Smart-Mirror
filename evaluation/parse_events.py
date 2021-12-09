from datetime import date, datetime

def formatTimeToList(outputList, fileLines, format):
    for line in fileLines:
        closeBracket = line.index(']')
        timestamp = line[1:closeBracket]

        to_datetime = datetime.strptime(timestamp, format)
        outputList.append(to_datetime)

jetson = open('TRIAL-Version.txt', 'r')
jet_lines = jetson.readlines()
list_pub = []
formatTimeToList(list_pub, jet_lines, "%Y-%m-%d %H:%M:%S.%f")

rasbpi = open('TRIAL-Version.txt', 'r')
ras_lines = rasbpi.readlines()
list_rec = []
formatTimeToList(list_rec, ras_lines, "%d.%m.%Y %H:%M.%S.%f")

lat_list = []

for i in range(len(list_pub)):
    diff = list_rec[i] - list_pub[i]
    lat_list.append(diff)

# Latency
[print(x.microseconds) for x in lat_list]

# Published
print("Published")
[print(x) for x in list_pub]

# Recieved
print("Recieved")
[print(x) for x in list_rec]