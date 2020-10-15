import csv
from person import Person
import random
import xml.etree.ElementTree as ET
import requests
import msgpack
import pandas as pd
import json

# Creating the CPR number.
def createCpr(DOB):
    random_4_numbers = random.randint(1000, 9999)
    return date[:2] + date[3:5] + date [6:] + str(random_4_numbers)


# Open the csv file.
with open("people.csv", newline='') as csvfile:
    peopleReader = csv.DictReader(csvfile)
    # Go through every person in the csv file.
    for row in peopleReader:
        # Create file structure for the xml file.
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
        headers = {'Content-Type': 'application/xml'}

          
        # Posting the xml body to 8080/nemID. 
        response = requests.post("http://localhost:8080/nemID", data=ET.tostring(person_obj), headers=headers)
        print(response)

        # Storing data as msgpack
        data = {
            "Firstname": firstName, "Lastname": lastName, "cprnumber": cpr, "Email": email
        }

        # Get the nemID
        data["NemID"] = json.loads(response.content.decode("UTF-8")).get("nemID", None)
        
        # Write msgpack file.
        with open(cpr+".msgpack", "wb") as outfile:
            packed = msgpack.packb(data)
            outfile.write(packed) 