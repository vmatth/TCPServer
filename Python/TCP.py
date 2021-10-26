#!/usr/bin/env python3

import socket
import xml.etree.ElementTree as ET
import csv
#import pandas as PD

HOST = '192.168.0.100'  
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                myroot = ET.fromstring(data)
                print('I recieved:', data)

                print('This is XML output:', myroot[0].text)
                print('This is XML output:', myroot[1].text)
                print('This is XML output:', myroot[2].text)

                with open('procssing_times_table.csv', 'rt') as csv_file:
                    csvmatrix = csv.reader(csv_file)
                    csvmatrix = list(csvmatrix)
                    row = int(myroot[1].text)-1
                    col = int(myroot[0].text)-1
                    SendData=csvmatrix[row][col]
                    print(SendData)
                    SendBytes=str.encode(SendData) 

                if not data:
                    break
                conn.sendall(SendBytes)