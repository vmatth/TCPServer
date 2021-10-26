#!/usr/bin/env python3

import socket
import xml.etree.ElementTree as ET
import csv
from tkinter import *



HOST = '172.20.66.121'  
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
                print("Bytes with ZEROS: ",data) #b'<GROUP_563><Station>9</Station><Carrier>9</Carrier><Date_Time>DT#2021-10-26-11:06:47</Date_Time></GROUP_563>\x00\x00'
                
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


                window = Tk()
                window.geometry('500x500')
                window.title("Welcome to LikeGeeks app")

                lbl1 = Label(window, text="Station: ", font=("Arial Bold", 30))
                lbl2 = Label(window, text=tree[0].text, font=("Arial Bold", 30))
                lbl1.grid(column=0, row=0)
                lbl2.grid(column=1, row=0)

                lbl3 = Label(window, text="Carrier: ", font=("Arial Bold", 30))
                lbl4 = Label(window, text=tree[1].text, font=("Arial Bold", 30))
                lbl3.grid(column=0, row=1)
                lbl4.grid(column=1, row=1)

                lbl5 = Label(window, text="Date and Time: ", font=("Arial Bold", 30))
                lbl6 = Label(window, text=tree[2].text, font=("Arial Bold", 30))
                lbl5.grid(column=0, row=2)
                lbl6.grid(column=1, row=2)

                window.mainloop()

                with open('procssing_times_table.csv', 'rt') as csv_file:
                    csvmatrix = csv.reader(csv_file)
                    csvmatrix = list(csvmatrix)
                    row = int(tree[1].text)-1
                    col = int(tree[0].text)-1
                    SendData=csvmatrix[row][col]
                    print(SendData)
                    SendBytes=str.encode(SendData) 
                    print("The type is : ", type(SendBytes))

                    lbl7 = Label(window, text="Delayed time: ", font=("Arial Bold", 30))
                    lbl8 = Label(window, text=SendData, font=("Arial Bold", 30))
                    lbl7.grid(column=0, row=3)
                    lbl8.grid(column=1, row=3)
                if not data:
                    break
                conn.sendall(SendBytes)
