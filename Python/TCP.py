#!/usr/bin/env python3

import socket
import xml.etree.ElementTree as ET
import csv
#import pandas as PD

HOST = '172.20.66.121'  
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Server on", HOST)
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024) #Data from PLC in bytes
                print(data) #b'<GROUP_563><Station>9</Station><Carrier>9</Carrier><Date_Time>DT#2021-10-26-11:06:47</Date_Time></GROUP_563>\x00\x00'
                
                string = data.decode('UTF-8') #Bytes enconded to string
                print(string) #<GROUP_563><Station>9</Station><Carrier>9</Carrier><Date_Time>DT#2021-10-26-11:06:47</Date_Time></GROUP_563>
                

                #Write the recieved data in type string to a xml file
                ##### Det er her det går galt, vi får 
                tree = ET.XML(string) 
                with open("xml.xml", "wb") as f:
                    f.write(ET.tostring(tree))

                #Open xml file
                mytree = ET.parse('xml.xml')
                myroot = mytree.getroot()
                print(myroot)

                print('Station', myroot[0].text)
                print('Carrier ID:', myroot[1].text)
                print('Date Time:', myroot[2].text)

                with open('procssing_times_table.csv', 'rt') as csv_file:
                    csvmatrix = csv.reader(csv_file)
                    csvmatrix = list(csvmatrix)
                    row = int(myroot[1].text)-1
                    col = int(myroot[0].text)-1
                    SendData=csvmatrix[row][col]
                    print(SendData)
                    SendBytes=str.encode(SendData) 
                    print("The type is : ", type(SendBytes))

                if not data:
                    break
                conn.sendall(SendBytes)
