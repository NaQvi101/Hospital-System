class Patient:
    def __init__(self,email, password,gender=None,dob=None,address=None,Phone_Number=None,name=None):
        self.name = name
        self.password = password
        self.email = email
        self.gender = gender
        self.dob = dob
        self.address = address
        self.Phone_Number = Phone_Number
class Doctor:
    def __init__(self,email,password,gender=None,address=None,dob=None,dateOfJoining=None,qualification=None,specialization=None,availability=None,Phone_Number=None,name=None):
        self.name = name
        self.password = password
        self.email = email
        self.gender = gender
        self.dob = dob
        self.dateOfJoining = dateOfJoining
        self.qualification = qualification
        self.specialization = specialization
        self.availability = availability
        self.Phone_Number = Phone_Number
        self.address = address


class Nurse:
    def __init__(self,email,password,name=None,gender=None, address=None ,dob=None,dateOfJoining=None,qualification=None,availability=None,Phone_Number=None):
        self.name = name
        self.password = password
        self.email = email
        self.gender = gender
        self.dob = dob
        self.dateOfJoining = dateOfJoining
        self.qualification = qualification
        self.availability = availability
        self.Phone_Number=Phone_Number        
        self.address = address
        
        
class Deal:
    def __init__(self,doctor_id,patient_id,symptoms,diagnosis=None,checkupfee=None,medicines=None,nurses=None):
        self.doctor_id=doctor_id
        self.patient_id=patient_id
        self.symptoms=symptoms
        self.diagnosis=diagnosis
        self.checkupfee=checkupfee
        self.medicines=medicines
        self.nurses=nurses

class Admin():
    def __init__(self,email,password):
        self.email=email
        self.password=password       