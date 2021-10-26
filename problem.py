#!/usr/bin/env python3

import xml.etree.ElementTree as ET

data = b'<GROUP_563><Station>9</Station><Carrier>9</Carrier><Date_Time>DT#2021-10-26-11:06:47</Date_Time></GROUP_563>\x00\x00' #data received from PLC in bytes
print(data)
string = data.decode('UTF-8') #Bytes to string
print(string)

#Write the data to a xml file
tree = ET.XML(string) #error here
with open("xml.xml", "wb") as f:
    f.write(ET.tostring(tree))
