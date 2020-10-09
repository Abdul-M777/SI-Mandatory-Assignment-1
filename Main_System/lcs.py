import csv
from person import Person
import random
import xml.etree.ElementTree as ET
import requests
import msgpack
import pandas as pd
import json

# Here we are creating the CPR number.
def createCpr(DOB):
    random_4_numbers = random.randint(1000, 9999)
    
    
    return date[:2] + date[3:5] + date [6:] + str(random_4_numbers)



with open("people.csv", newline='') as csvfile:
    peopleReader = csv.DictReader(csvfile)
    for row in peopleReader:

        firstName = row["FirstName"]
        lastName = row['LastName']
        email = row['Email']
        date = row['DateOfBirth']


        cpr = createCpr(date)
        

        person_obj = ET.Element("Person")
    
        ET.SubElement(person_obj, "FirstName").text = firstName
        ET.SubElement(person_obj, "LastName").text = lastName
        ET.SubElement(person_obj, "cprnumber").text = cpr
        ET.SubElement(person_obj, "email").text = email
        
        tree = ET.ElementTree(person_obj)
        tree.write(firstName + ".xml")
        headers = {'Content-Type': 'application/xml'}

        # # Here we send 
        # with open('Cpr.xml') as xml:
        response = requests.post("http://localhost:8080/nemID", data=ET.tostring(person_obj), headers=headers)
        json.loads(response.content)["nemID"]
        print(response)

        data = {
            "Firstname": firstName, "Lastname": lastName, "cprnumber": cpr, "Email": email
        }

        

        with open(firstName+".msgpack", "wb") as outfile:
            packed = msgpack.packb(data)
            outfile.write(packed) 



# Here we open the people.csv file and we use the rows from the csv file in the addPeople method.


# Here we create the xml file and we call it Cpr.xml.


#   
