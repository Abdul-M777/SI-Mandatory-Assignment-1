import csv
from person import Person
import random
import xml.etree.ElementTree as ET
import requests
import msgpack
import pandas as pd
import json

# Here we are creating the CPR number.
# def createCpr(DOB):
    
    # return 



# People = ET.Element('People')
# In this method we add the people from the people.csv to the Xml file.
# def addPeople(firstName, lastName, DOB, email):
#     peopleArr = []
#     cpr = createCpr(DOB)
#     person = Person(firstName, lastName, DOB, email, cpr)
#     person.is_valid()
    
    
#     data = {
#         "FirstName": person.FirstName, "LastName": person.LastName, "CprNumber": person.Cpr, "Email": person.Email
#     }


    

# peopleArr.append(person)
# df = pd.read_csv("people.csv")
with open("people.csv", newline='') as csvfile:
    peopleReader = csv.DictReader(csvfile)
    for row in peopleReader:

        firstName = row["FirstName"]
        lastName = row['LastName']
        email = row['Email']
        date = row['DateOfBirth']

        random_4_numbers = random.randint(1000, 9999)
        cpr = date[:2] + date[3:5] + date [6:] + str(random_4_numbers)

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
