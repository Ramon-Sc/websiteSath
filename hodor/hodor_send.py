#!/usr/bin/env python3

from datetime import timedelta
from datetime import datetime
import json
import socket
import time


def get_data():
    #Open:bool, OpenSince/LastOpen:int, OpenTimeSum:int    
    data = {}
    data["status"] = False
    data["since"] = 0
    data["sum"] = timedelta(seconds = 0) 
    data["day"] = ""
    heatmap_data = [[0 for hour in range(24)] for _ in range(7)]
    lastdt = 0

    with open("log") as log:
        for line in log:
            parts = line.split(" ") 
            dt = datetime.fromtimestamp(int(parts[0])) 

            if lastdt != 0 and "close" in parts[1]:
                delta = dt - lastdt 
                heatmap_data[lastdt.weekday()][lastdt.hour] += delta.seconds//3600
                data["sum"] += delta
            lastdt = dt 


    data["status"] = ("open" in parts[1])
    data["since"] = dt.strftime('%H:%M')

    if datetime.now() - dt < timedelta(days=1): 
        data["day"] = "heute"
    if datetime.now() - dt > timedelta(days=1): 
        data["day"] = "gestern"
    if datetime.now() - dt > timedelta(days=2): 
        data["day"] = "vorgestern"
    if datetime.now() - dt > timedelta(days=3): 
        data["day"] = dt.strftime('%d.%m.%Y') 


    data["sum"] = str(data["sum"]) 
    data["status"] = "OFFEN" if data["status"] else  "GESCHLOSSEN"

    return heatmap_to_json(heatmap_data), json.dumps(data)

def heatmap_to_json(data):

    json = "["

    for weekday, week in enumerate(data):
        for hour, value in enumerate(week):
            json += "{" + '"day": ' + str(weekday+1) + ', "hour": ' + str(hour+1) + ', "value": '+ str(value) + "},"

    return json[:-1]+"]" 



###### MAIN ####### 

host = socket.gethostname() 
port = 12312
switch = True

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    heatmap, current = get_data()
    s.connect((host,port))

    if switch:
        s.sendall(str(current).encode()) 
    else:
        s.sendall(heatmap.encode()) 

    switch = not switch 

    time.sleep(30)
    s.close()
