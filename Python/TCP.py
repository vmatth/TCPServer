#!/usr/bin/env python3

import socket
import xml.etree.ElementTree as ET
import csv



HOST = '172.20.66.64'  
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Server on", HOST) #Server on 172.20.66.121
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr) #Connected by ('172.20.1.1', 60077)
            while True:
                data2 = conn.recv(1024) #Data from PLC in bytes
                print("Bytes with ZEROS: ",data2) #b'<GROUP_563><Station>9</Station><Carrier>9</Carrier><Date_Time>DT#2021-10-26-11:06:47</Date_Time></GROUP_563>\x00\x00'
                
                #Fix the bytes data by removing x00 and other bytes that are irrelevant
                data_list = list(data2)
                #print("Data List" , data_list)
                count = data_list.count(0)
                print(count)
                data = data2[:-count]   # fjerner de sidste værdier med \x00\x00 i 
                
                #data received from PLC in bytes
                print("Bytes without ZEROS: ",data)
                string = data.decode() #Bytes to string
                print("String to XML-parser",string)
                
                #Write the data to a xml object
                tree = ET.fromstring(string) 

                # Printing name tag and content
                print(tree[0].tag, tree[0].text)
                print(tree[1].tag, tree[1].text)
                print(tree[2].tag, tree[2].text)



                with open('procssing_times_table.csv', 'rt') as csv_file:
                    csvmatrix = csv.reader(csv_file)
                    csvmatrix = list(csvmatrix)
                    row = int(tree[1].text)-1
                    col = int(tree[0].text)-1
                    SendData=csvmatrix[row][col]
                    print("Data sent", SendData)
                    SendBytes=str.encode(SendData) 

                if not data:
                    break
                conn.sendall(SendBytes)
                # Save data to txt file
                with open('Data_group563.txt', 'a') as f:
                    f.write('Date and time: ')
                    f.write(tree[2].text)
                    f.write('\n')
                    f.write('Station ID: ')
                    f.write(tree[1].text)
                    f.write('\n')
                    f.write('Carrier ID: ')
                    f.write(tree[0].text)
                    f.write('\n')
                    f.write('Process time: ')
                    f.write(SendData)
                    f.write('\n')
                    f.write('\n')
                    f.close()
