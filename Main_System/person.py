from datetime import datetime

class Person:
    def __init__(self, f_name, l_name, date_of_birth, email, cpr, nemID=None):
        self.FirstName = f_name
        self.LastName = l_name
        self.DateOfBirth = date_of_birth
        self.Email = email
        self.Cpr = cpr
        self.nemID = nemID

    def validate_date_of_birth(self):
        try:
            datetime.strptime(self.DateOfBirth, '%d-%m-%Y')
        except:
            raise ValueError("Incorrect data format...")

    
    def is_valid(self):
        if self.FirstName == "" or self.LastName == "" or self.Email == "" or self.DateOfBirth == "" :
            raise ValueError
        return True
        