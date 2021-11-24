from views import *
import pymysql
class hospitalModel:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        try:
            self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                              database=self.database)
        except Exception as e:
            print("There is error in connection", str(e))

    def _del_(self):
        if self.connection != None:
            self.connection.close()
    
    def checkPatientExist(self, patient):
        flag = False
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select email from patient")
                emailList = cursor.fetchall()
                for e in emailList:
                    if patient.email == e[0]:
                        flag = True
                        break
        except Exception as e:
            print("Exception in checkPatientExist", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag
        
    
    def loginDoctor(self, doctor):
        flag = False
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "Select email,password from doctors where email=%s and password=%s"
                args = (doctor.email, doctor.password)
                cursor.execute(query, args)
                record = cursor.fetchone()
                if record[0] == doctor.email and record[1] == doctor.password:
                    flag = True
        except Exception as e:
            print("Exception in loginDoctor", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag    
        
        
    def loginPatient(self, patient):
        flag = False
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "Select email,password from patients where email=%s and password=%s;"
                args = (patient.email, patient.password)
                cursor.execute(query, args)
                record = cursor.fetchone()
                if record[0] == patient.email and record[1] == patient.password:
                    flag = True
        except Exception as e:
            print("Exception in loginPatient", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag
        
        
    def loginAdmin(self, admin):
        flag = False
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "Select email,password from admins where email=%s and password=%s"
                args = (admin.email, admin.password)
                cursor.execute(query, args)
                record = cursor.fetchone()
                if record[0] == admin.email and record[1] == admin.password:
                    flag = True
        except Exception as e:
            print("Exception in loginAdmin", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag
    
    
    def getPatientName(self,email):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "Select name from patients where email=%s"
                args = (email)
                cursor.execute(query, args)
                record = cursor.fetchone()
                return record[0]
        except Exception as e:
            print("Exception in getPatientName", str(e))
        finally:
            if cursor != None:
                cursor.close()
        

    def getDoctorName(self,email):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "Select name from doctors where email=%s"
                args = (email)
                cursor.execute(query, args)
                record = cursor.fetchone()
                return record[0]
        except Exception as e:
            print("Exception in getDoctorName", str(e))
        finally:
            if cursor != None:
                cursor.close()
                
    
    
        
    def insertDoctor(self, doctor):
        cursor = None
        flag = False
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "insert into doctors (Name,Email,Address,Phone_Number,Password,DOB,Gender,JoiningDate,Specialization,Availability,Qualification) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                args = (doctor.name,doctor.email,doctor.address,doctor.Phone_Number,doctor.password,doctor.dob,doctor.gender, doctor.dateOfJoining,doctor.specialization,
                doctor.availability,doctor.qualification)
                cursor.execute(query, args)
                self.connection.commit()
                flag = True
        except Exception as e:
            print("Exception in insertDoctor", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag
    

    def insertPatient(self, patient):
            cursor = None
            flag = False
            try:
                if self.connection != None:
                    cursor = self.connection.cursor()
                    query = "insert into patients (Name,Address,Phone_Number,Password,Gender,DOB,Email) values (%s,%s,%s,%s,%s,%s,%s)"
                    args = (patient.name, patient.address, patient.Phone_Number, patient.password, patient.gender, patient.dob, patient.email)
                    cursor.execute(query, args)
                    self.connection.commit()
                    flag = True
            except Exception as e:
                print("Exception in insertPatient", str(e))
            finally:
                if cursor != None:
                    cursor.close()
                return flag
            
    def insertNurse(self, nurse):
            cursor = None
            flag = False
            try:
                if self.connection != None:
                    cursor = self.connection.cursor()
                    query = "insert into nurses (Name,Password,Phone_Number,Email,Gender,DOB,JoiningDate,Availability,Qualification) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    args = (nurse.name, nurse.password, nurse.Phone_Number, nurse.email, nurse.gender, nurse.dob, nurse.dateOfJoining, nurse.availability, nurse.qualification)
                    cursor.execute(query, args)
                    self.connection.commit()
                    flag = True
            except Exception as e:
                print("Exception in insertNurse", str(e))
            finally:
                if cursor != None:
                    cursor.close()
                return flag
    
    
    def deleteDoctor(self, id):
        cursor = None
        flag = False
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "delete from doctors where doc_id=%s"
                args = (id)
                cursor.execute(query, args)
                self.connection.commit()
                flag = True
        except Exception as e:
            print("Exception in deleteDoctor", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag
        
    def checkPatientExist(self,pateint):
        cursor=None
        flag=False
        try:
            if self.connection!=None:
                cursor = self.connection.cursor()
                query = "select email from patients;"
                cursor.execute(query)
                for d in cursor.fetchall():
                    if d[0]==pateint.email:
                        flag=True
                        break
        except Exception as e:
            print("Exception in CheckPatientExist: ", str(e))
        finally:
            if cursor!=None:
                cursor.close()
                return flag
            
    def checkDoctorExist(self,doctor):
        cursor=None
        flag=False
        try:
            if self.connection!=None:
                cursor = self.connection.cursor()
                query = "select email from doctors;"
                cursor.execute(query)
                for d in cursor.fetchall():
                    if d[0]==doctor.email:
                        flag=True
                        break
        except Exception as e:
            print("Exception in CheckDoctorExist: ", str(e))
        finally:
            if cursor!=None:
                cursor.close()
                return flag
    
    
    def deletePatient(self, id):
        cursor = None
        flag = False
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "delete from patients where patient_id=%s"
                args = (id)
                cursor.execute(query, args)
                self.connection.commit()
                flag = True
        except Exception as e:
            print("Exception in deletePatient", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag
    
    
    def checkNurseExist(self,nurse):
        cursor=None
        flag=False
        try:
            if self.connection!=None:
                cursor = self.connection.cursor()
                query = "select email from nurses;"
                cursor.execute(query)
                for d in cursor.fetchall():
                    if d[0]==nurse.email:
                        flag=True
                        break
        except Exception as e:
            print("Exception in CheckNurseExist: ", str(e))
        finally:
            if cursor!=None:
                cursor.close()
                return flag
    
    def allDoctors(self):
        cursor=None
        try:
            if self.connection!=None:
                cursor = self.connection.cursor()
                query = "select doc_id,name,email,Address,gender,dob,Phone_Number,joiningdate,Qualification,Specialization,Availability from doctors;"
                cursor.execute(query)
                data = cursor.fetchall()
                return data
        except Exception as e:
            print("Exception in allDoctors: ", str(e))
        finally:
            if cursor!=None:
                cursor.close()
                return data 
     
     
    def allPatients(self):
        cursor=None
        try:
            if self.connection!=None:
                cursor = self.connection.cursor()
                query = "select patient_id,name,email,gender,dob,address,phone_number from patients;"
                cursor.execute(query)
                data = cursor.fetchall()
                return data
        except Exception as e:
            print("Exception in CheckPatient Exist: ", str(e))
        finally:
            if cursor!=None:
                cursor.close()
                             
    def allNurses(self):
        cursor=None
        try:
            if self.connection!=None:
                cursor = self.connection.cursor()
                query = "select nurse_id,name,email,gender,dob,phone_number,qualification,joiningdate,Availability from nurses;"
                cursor.execute(query)
                data = cursor.fetchall()
                return data
        except Exception as e:
            print("Exception in CheckPatient Exist: ", str(e))
        finally:
            if cursor!=None:
                cursor.close()
                
    
    def deleteNurse(self, id):
        cursor = None
        flag = False
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "delete from nurses where nurse_id=%s"
                args = (id)
                cursor.execute(query, args)
                self.connection.commit()
                flag = True
        except Exception as e:
            print("Exception in deleteNurse", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag
        
        
        
        
        
    def selectSpecializeDoctor(self, specialization):#patient
        cursor = None
        data = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select doc_id,name,availability from doctors where Specialization=%s"
                cursor.execute(query, specialization)
                data = cursor.fetchall()
        except Exception as e:
            print("Exception in selectSpecializeDoctor", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return  data

    def getSpecialization(self):
        cursor = None
        data = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select DISTINCT Specialization from doctors;"
                cursor.execute(query)
                data = cursor.fetchall()
        except Exception as e:
            print("Exception in getSpecialization", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return  data
        
    def viewLatestReport(self, pid):# show current report
        cursor = None
        data = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select deal_id from deal where patient_id=%s"
                cursor.execute(query, pid)
                deal_id = cursor.fetchall()
                deal_id = deal_id[-1]
                query = "select deal.deal_id,doctors.name,deal.symptoms,deal.diagnosis,deal.medicines,deal.checkup_fee from deal,doctors where deal.deal_id=%s and deal.doc_id=doctors.doc_id"
                cursor.execute(query, deal_id[0])
                data = cursor.fetchone()
        except Exception as e:
            print("Exception in viewCurrentReport", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return data


    def getPatientId(self, email):
        data = None
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select patient_id from patients where email=%s;"
                args=(email)
                cursor.execute(query,args)
                data = cursor.fetchone()
                return data
        except Exception as e:
            print("Exception in getPatientId", str(e))
        finally:
            if cursor != None:
                cursor.close()
            


    def myAllReports(self, pid):#Patients Previous aur Latest Reports
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query="select deal_id from deal where patient_id=%s;"
                arg = (pid)
                cursor.execute(query, arg)
                deal_id = cursor.fetchall()
                data = []
                for i in range(0,len(deal_id)):
                    query="select deal.deal_id,doctors.name,deal.symptoms,deal.diagnosis,deal.medicines,deal.checkup_fee from deal,doctors where deal.deal_id=%s and deal.doc_id=doctors.doc_id;"
                    args = (deal_id[i][0])
                    cursor.execute(query,args)
                    d = cursor.fetchone()
                    data.append(d)
                return data
        except Exception as e:
            print("Exception in viewAllReport", str(e))
        finally:
            if cursor != None:
                cursor.close()
                
    def viewCurrentPatient(self, doc_id):
        data = None
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select deal_id,deal.patient_id,patients.name,patients.gender,deal.symptoms from deal,patients where deal.doc_id=%s and deal.patient_id=patients.patient_id and deal.checkup_fee=0"
                cursor.execute(query,doc_id)
                data = cursor.fetchone()
                
        except Exception as e:
            print("Exception in viewCurrentPatient", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return data


    def getDoctorId(self, email):
        data = None
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select doc_id from doctors where email=%s"
                args=(email)
                cursor.execute(query,args)
                data = cursor.fetchone()
                data = data[0]
        except Exception as e:
            print("Exception in getDoctorId", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return data

    def getAdminId(self, email):
        data = None
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select admin_id from admins where email=%s"
                args=(email)
                cursor.execute(query,args)
                data = cursor.fetchone()
                data = data[0]
        except Exception as e:
            print("Exception in getAdminId", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return data
    

    def updateDoctorDeal(self, deal_id , diagnosis, checkup_fee, medicines):
        cursor = None
        flag = False
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "Update deal set diagnosis=%s, checkup_fee=%s, medicines=%s where deal_id=%s ; "
                args=(diagnosis,int(checkup_fee) , medicines , deal_id)
                cursor.execute(query,args)
                self.connection.commit()
                flag = True
        except Exception as e:
            print("Exception in updateDoctorDeal", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag        

    def viewWaitingPatient(self, doc_id):
        data = None
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select deal.patient_id,patients.name,patients.gender,deal.symptoms from deal,patients where deal.doc_id=%s and deal.patient_id=patients.patient_id and deal.checkup_fee=0"
                cursor.execute(query,doc_id)
                data = cursor.fetchall()
                data = data[1:]
        except Exception as e:
            print("Exception in viewWaitingPatient", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return data
        
    def addPatientDeal(self, doc_id, p_id, symptoms):
        flag = False
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select nurse_id from nurses where availability=%s"
                cursor.execute(query,'1')
                nid = cursor.fetchone()
                print(nid)
                nurse_name = None
                if nid is not None:
                    nid = nid[0]
                    query="Select name from nurses where nurse_id=%s"
                    cursor.execute(query,nid)
                    nurse_name=cursor.fetchone()
                    nurse_name=nurse_name[0]
                print(doc_id,p_id)
                query = "insert into deal(doc_id,patient_id,symptoms,diagnosis,checkup_fee,medicines,nurses) values (%s,%s,%s,%s,%s,%s,%s)"
                args = (p_id, doc_id, symptoms, '', 0, '', None if nurse_name==None else nurse_name)
                cursor.execute(query, args)
                self.connection.commit()
                query = "update nurses set availability='0' where nurse_id=%s"
                cursor.execute(query, nid)
                self.connection.commit()
                flag = True
        except Exception as e:
            print("Exception in addDeal", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return flag
        
        
    def selectSpecializeDoctor(self, specialization):#patient
        cursor = None
        data = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select doc_id,name,availability from doctors where Specialization=%s"
                cursor.execute(query, specialization)
                data = cursor.fetchall()
        except Exception as e:
            print("Exception in selectSpecializeDoctor", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return  data

    def getSpecialization(self):
        cursor = None
        data = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select DISTINCT Specialization from doctors"
                cursor.execute(query)
                data = cursor.fetchall()
        except Exception as e:
            print("Exception in getSpecialization", str(e))
        finally:
            if cursor != None:
                cursor.close()
            return  data