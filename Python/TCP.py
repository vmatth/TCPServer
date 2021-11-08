#!/usr/bin/env python3

import socket
import xml.etree.ElementTree as ET
import csv

HOST = '172.20.66.64'  
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Server on", HOST) #Server on 172.20.66.121
    s.bind((HOST, PORT)) #Create the server with a specified HOST and PORT
    s.listen() #Listen for incoming clients
    while True: #Redundant :(
        conn, addr = s.accept() #Client connect
        with conn:
            print('Connected by', addr) #Print Connected by ('172.20.1.1', 60077)
            while True: #While loop, to keep receiving PLC data
                data2 = conn.recv(1024) #Data from PLC in bytes with unknown bytes at the end

                #Fix the bytes data by removing x00 and other bytes that are irrelevant
                data_list = list(data2) #Convert bytes into int list
                count = data_list.count(0)
                data = data2[:-count]   # Removes \x00\x00 bytes 
                
                string = data.decode() #Bytes to string
                
                #Write the data to a xml object
                tree = ET.fromstring(string) 

                # Printing name tag and content
                print(tree[0].tag, tree[0].text) #Station ID
                print(tree[1].tag, tree[1].text) #Carrier ID
                print(tree[2].tag, tree[2].text) #Date time


                #Unpack csv file into a 2D array/matrix to find time (ms) for the carrier to wait
                with open('procssing_times_table.csv', 'rt') as csv_file:
                    csvmatrix = csv.reader(csv_file)
                    csvmatrix = list(csvmatrix)
                    row = int(tree[1].text)-1
                    col = int(tree[0].text)-1
                    SendData=csvmatrix[row][col]
                    print("Data sent", SendData)
                    print("\n")
                    SendBytes=str.encode(SendData) #Converts milliseconds from string to bytes

                if not data: #If data doesn't exist then break (redundant since it always works)
                    break
                conn.sendall(SendBytes) #Sends miliseconds as bytes
                # Save data to txt file
                with open('Data_group563.txt', 'a') as f:
                    f.write('Date and time: ')
                    f.write(tree[2].text)
                    f.write('\n')
                    f.write('Station ID: ')
                    f.write(tree[0].text)
                    f.write('\n')
                    f.write('Carrier ID: ')
                    f.write(tree[1].text)
                    f.write('\n')
                    f.write('Process time: ')
                    f.write(SendData)
                    f.write('\n')
                    f.write('\n')
                    f.close()
