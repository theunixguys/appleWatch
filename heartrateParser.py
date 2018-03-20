#!/usr/bin/python3


import subprocess
import time
import datetime
import requests
influxAPI = 'http://127.0.0.1:8086/write?db=heartrate'


with open('hr.csv') as myFile:
    contents = myFile.readlines()
    print(contents)

lastTime = 100
lastIncrement = 0

for line in contents:
    hrFields = line.split(',')
    myDate = hrFields[0]
    myHR = hrFields[2]
    myHR = myHR.rstrip()
    timeFormat = "%d-%b-%Y %H:%M"
    mydt = int(time.mktime(time.strptime(hrFields[0], timeFormat)))
    mydtNanoSecs = mydt * 1000000000
    if mydtNanoSecs == lastTime:
       if lastIncrement:
          mydtNanoSecs = lastIncrement + 2000000000
          lastIncrement = mydtNanoSecs
       else:
          mydtNanoSecs = mydtNanoSecs + 2000000000
          lastIncrement = mydtNanoSecs
    else:
       lastTime = mydtNanoSecs
       lastIncrement = mydtNanoSecs

    payload1 = "rates,user=aaron rate=" + str(myHR) + " " + str(mydtNanoSecs)

    r = requests.post(influxAPI, data=payload1)
    #print(r.headers)
    print(mydtNanoSecs)
