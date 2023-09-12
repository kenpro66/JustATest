import xml.etree.ElementTree as ET
import os

def ping(ip_address):
    response = os.system("ping -c 1 " + ip_address + " > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

# parse the XML file
#tree = ET.parse("/Users/kennethprochaska/Documents/JustATest/UnitTesting/scan.xml")
tree = ET.parse("/Users/kennethprochaska/scan.out")
root = tree.getroot()

# loop through elements
#for elem in root.iter("address"):
#    print(elem.tag, elem.attrib)

# loop through all elements in the xml file
for element in root.iter():
    # check if the element has attributes
    if len(element.attrib) > 0:
        # loop through all the attributes of the element
        for key, value in element.attrib.items():
            if key=='addr':
                #print(f"Attribute Name: {key}, Attribute Value: {value}")
                if ping(value):
                    print(value + " is reachable")
                else:
                    print(value + " is not reachable")

