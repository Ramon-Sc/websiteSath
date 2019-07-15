#!/usr/bin/env python3

import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname() 
port = 12312
serversocket.bind((host, port)) 

while True:
    serversocket.listen(1)

    connection, addr = serversocket.accept()
    #print("Got a connection from %s" % str(addr))

    try: 
        data = connection.recv(20480).decode()

        if "status" in data:
            with open("current.json", "w+") as json:
                print("recived current.json")
                json.write(data)
        elif "value" in data:
            with open("heatmap.json", "w+") as json:
                print("recived schmutz.json")
                json.write(data)
        elif len(data) > 0:
            print("Unknown data recived")
            print(data) 
            print("---end")
            break
        connection.close() 

    except Exception as e: 
        print(e) 
        connection.close()
        time.sleep(1)
        break
