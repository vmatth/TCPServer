#!/usr/bin/env python3

import xml.etree.ElementTree as ET
data2 = b'<GROUP_563><Station>9</Station><Carrier>9</Carrier><DateTime>DT#2021-10-26-11:06:47</DateTime></GROUP_563>\x00\x00'

#Fix the bytes data by removing x00 and other bytes that are irrelevant
data_list = list(data2)
print("Data List" , data_list)
count = data_list.count(0)
print(count)
# i = data_list.index(0)
# print("ind ", i)
# while i < len(data_list):
#   print("Removing from list: ", data_list[i])
#   i = i + 1
#   #remove index her :D

data = data2[:-count]   # fjerner de sidste værdier med \x00\x00 i 
  
#data received from PLC in bytes
print("aa2")
print(data)
print("aa3")
string = data.decode() #Bytes to string
print(string)
print("aa4")
string1 = '<GROUP_563><Station>9</Station><Carrier>9</Carrier><DateTime>DT#2021-10-26-11:06:47</DateTime></GROUP_563>'
print(string1)
#Write the data to a xml file
tree = ET.fromstring(string) #error here
#tree = ET.XML(string) #error here
print("aa5")



for child in tree:
    print(child.tag,child.text)

#with open("xml.xml", "wb") as f:
#    f.write(ET.tostring(tree))
print("aa6")

