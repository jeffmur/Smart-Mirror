from gpiozero import *
import psutil
from time import sleep
cpu = CPUTemperature()
import json

while True:
    sleep(5)
    # gives a single float value
    cpuUsage = psutil.cpu_percent()
    print("CPU Usage: ", cpuUsage)
    print("    Temp : ", cpu.temperature)
    # gives an object with many fields
    psutil.virtual_memory()
    # you can convert that object to a dictionary 
    dict(psutil.virtual_memory()._asdict())
    # you can have the percentage of used RAM
    ramUsage = psutil.virtual_memory().percent
    print("Ram Usage: ", ramUsage)

    myData = {
        "CPU Usage": cpuUsage,
        "CPU Temp": cpu.temperature, 
        "RAM Usage": ramUsage 
    }

    with open('log_monitor.txt', 'a') as outfile: 
        json.dump(myData, outfile)

