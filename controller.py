from hospitalModel import hospitalModel
from views import *
from flask import Flask,render_template,request,url_for,redirect

def getModel():
    return hospitalModel("127.0.0.1","root","1010","myhospitaldb")

app = Flask(__name__)



@app.route('/')
def  homePage():
    return render_template('login.html',error=False,errorMsg=None,title="HMS-Login")

pname=None
email=None

@app.route('/login',methods=['Post'])
def login():
    global pname,email
    email = request.form["email"]
    password = request.form["password"]
    loginType = request.form["logintype"]
    model =  getModel()
    if loginType == "patient":
        patient = Patient(email,password)
        if model.loginPatient(patient):
            pname = model.getPatientName(email)
            return render_template("patientMain.html",name = pname,title=f"{ model.getPatientName(email)} Patient - HMS") 
    elif loginType == "doctor":
        doctor = Doctor(email,password)
        if model.loginDoctor(doctor):
            pname = model.getDoctorName(email)
            return render_template("docMain.html",name = pname) 
    elif loginType == "admin":
        admin = Admin(email,password)
        if model.loginAdmin(admin):
            return render_template("adminMain.html") 
    return render_template("login.html",error=True,errorMsg="Incorrect Email or Password",title="HMS-Login")



@app.route('/adminMain')
def adminMain():
    return render_template("adminMain.html",title="Admin-Main HMS")


@app.route('/patientSignUp')
def patientSignUp():
    return render_template("patientSignUp.html",error=False,errorMsg=None,success=False,successMsg=None,title="New Patient-HMS")
    
    
@app.route('/patientsignupSubmit',methods=["post"])
def patientsignupSubmit():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    gender = request.form["gender"]
    Phone_Number = request.form["phone"]
    dob = request.form["dob"]
    address=request.form["address"]
    patient = Patient(name=name, password=password, email=email, gender=gender, dob=dob, address=address, Phone_Number=Phone_Number)
    model = getModel()
    if model.checkPatientExist(patient):
        return render_template("patientSignUp.html",error=True,errorMsg="Email already Exist.",success=False,successMsg = None,title="New Patient-HMS")
    else:
        model.insertPatient(patient)
        return render_template("patientSignUp.html",error=False,errorMsg=None,success=True,successMsg="Account Created now you can login as patient.",title="New Patient-HMS")
        
        
@app.route('/patientSignUpByAdmin')
def patientSignUpByAdmin():
    return render_template("signupPatientbyadmin.html",error=False,errorMsg=None,success=False,successMsg=None,title="New Patient-HMS")
        

@app.route('/patientSignUpByAdminSubmit', methods=["post"])
def patientSignUpByAdminSubmit():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    gender = request.form["gender"]
    Phone_Number = request.form["phone"]
    dob = request.form["dob"]
    address=request.form["address"]
    patient = Patient(name=name, password=password, email=email, gender=gender, dob=dob, address=address, Phone_Number=Phone_Number)
    model = getModel()
    if model.checkPatientExist(patient):
        return render_template("signupPatientbyadmin.html",error=True,errorMsg="Patient with that Email Address Already Exists.",success=False,successMsg = None,title="New Patient-HMS")
    else:
        model.insertPatient(patient)
        return render_template("signupPatientbyadmin.html",error=False,errorMsg=None,success=True,successMsg="Patient Added Successfully.",title="New Patient-HMS")    
    
    
@app.route('/addDoctor')
def addDoctor():
        return render_template("doctorSignUp.html",error=False,errorMsg=None,success=False,successMsg=None,title="New Doctor-HMS")    
    
@app.route('/newDoctorSubmit', methods=["post"])
def newDoctorSubmit():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    gender = request.form["gender"]
    Phone_Number = request.form["phone"]
    dob = request.form["dob"]
    address=request.form["address"]
    qualification=request.form["qualification"]
    doj=request.form["doj"]
    specializalition=request.form["specialization"]
    doctor = Doctor(name=name,email=email, password=password,gender=gender,address=address,Phone_Number=Phone_Number,specialization=specializalition,
                    availability=True,dateOfJoining=doj,qualification=qualification,dob=dob)
    model = getModel()
    if model.checkDoctorExist(doctor):
        return render_template("doctorSignUp.html",error=True,errorMsg="Doctor with that EmailAddress Already Exist.",success=False,successMsg = None,title="New Doctor-HMS")
    else:
        print(model.insertDoctor(doctor))
        return render_template("doctorSignUp.html",error=False,errorMsg=None,success=True,successMsg="Doctor Added Successfully.",title="New Doctor-HMS")    

@app.route('/addNurse')
def addNurse():
    return render_template("nurseSignUp.html",error=False,errorMsg=None,success=False,successMsg=None,title="New Doctor-HMS")    
@app.route('/newNurseSubmit',methods=['post'])
def newNurseSubmit():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    gender = request.form["gender"]
    Phone_Number = request.form["phone"]
    dob = request.form["dob"]
    address=request.form["address"]
    qualification=request.form["qualification"]
    doj=request.form["doj"]

    nurse = Nurse(name=name,email=email, password=password,gender=gender,address=address,Phone_Number=Phone_Number,
                    availability=True,dateOfJoining=doj,dob=dob,qualification=qualification)
    model = getModel()
    if model.checkNurseExist(nurse):
        return render_template("nurseSignUp.html",error=True,errorMsg="Nurse with that EmailAddress Already Exist.",success=False,successMsg = None,title="New Nurse-HMS")
    else:
        model.insertNurse(nurse)
        return render_template("nurseSignUp.html",error=False,errorMsg=None,success=True,successMsg="Nurse Added Successfully.",title="New Nurse-HMS")    

@app.route('/showAllPatients')
def adminPatientsView():
    model = getModel()
    patients = model.allPatients()
    length = len(patients)    
    return render_template("showAllPatients.html",len=True if length!=0 else False, patients=patients,title="Patients-Data HMS") 




@app.route("/deleteNurses")
def deleteNurses():
    model = getModel()
    nurses = model.allNurses()
    length=len(nurses)
    if length!=0:
        return render_template("deleteNurses.html",len=True,nurses=nurses,error=False,errorMsg=None , success=False,successMsg=None)
    else:
        return render_template("deleteNurses.html",len=False,nurses=nurses,error=False,errorMsg=None , success=False,successMsg=None)

@app.route('/deleteNursesSubmit',methods=['post'])
def deleteNursesSubmit():
    flag=False
    ids = request.form.getlist("deleteNurse")
    if len(ids)!=0:
        flag=True
        model=getModel()
        for id in ids:
            model.deleteNurse(int(id))
    model = getModel()
    nurses = model.allNurses()
    length=len(nurses)
    if flag:
        return render_template("deleteNurses.html",len=True if length!=0 else False ,nurses=nurses,error=False,errorMsg=None, success=True,successMsg="Nurses Deleted Successfully")
    else:
        return render_template("deleteNurses.html",nurses=nurses,len=True if length!=0 else False ,error=True,errorMsg="Please select atleast one Nurse", success=False,successMsg=None)

@app.route("/deletePatients")
def deletePatients():
    model = getModel()
    patients = model.allPatients()
    length=len(patients)
    if length!=0:
        return render_template("deletePatients.html",len=True,patients=patients,error=False,errorMsg=None , success=False,successMsg=None)
    else:
        return render_template("deletePatients.html",len=False,patients=patients,error=False,errorMsg=None , success=False,successMsg=None)
@app.route("/deletePatientsSubmit",methods=["post"])
def deletePatientsSubmit():
    flag=False
    ids = request.form.getlist("deletePatient")
    if len(ids)!=0:
        flag=True
        model=getModel()
        for id in ids:
            model.deletePatient(int(id))
    model = getModel()
    patients = model.allPatients()
    length=len(patients)
    if flag:
        return render_template("deletePatients.html",len=True if length!=0 else False ,patients=patients,error=False,errorMsg=None, success=True,successMsg="Patients Deleted Successfully")
    else:
        return render_template("deletePatients.html",patients=patients,len=True if length!=0 else False ,error=True,errorMsg="Please select atleast one patient", success=False,successMsg=None)
        
@app.route('/showAllNurses')    
def adminNursesView():
    model = getModel()
    nurses = model.allNurses()
    length = len(nurses)    
    return render_template("showAllNurses.html",len=True if length!=0 else False, nurses=nurses,title="Nurses-Record HMS")    



@app.route('/showAllDoctors')    
def adminDoctorsView():
    model = getModel()
    doctors = model.allDoctors()
    length = len(doctors)    
    return render_template("showAllDoctors.html",len=True if length!=0 else False, doctors=doctors,title="Doctors-Record HMS")    
    
    


@app.route("/deleteDoctors")
def deleteDoctors():
    model = getModel()
    doctors = model.allDoctors()
    length=len(doctors)
    if length!=0:
        return render_template("deleteDoctors.html",len=True,doctors=doctors,error=False,errorMsg=None , success=False,successMsg=None,title="Patients Delete-HMS")
    else:
        return render_template("deleteDoctors.html",len=False,doctors=doctors,error=False,errorMsg=None , success=False,successMsg=None,title="Patients Delete-HMS")


@app.route('/deleteDoctorsSubmit',methods=['post'])
def deleteDoctorsSubmit():
    flag=False
    ids = request.form.getlist("deleteDoctor")
    if len(ids)!=0:
        flag=True
        model=getModel()
        for id in ids:
            model.deleteDoctor(int(id))
    model = getModel()
    doctors = model.allDoctors()
    length=len(doctors)
    if flag:
        return render_template("deleteDoctors.html",len=True if length!=0 else False ,doctors=doctors,error=False,errorMsg=None, success=True,successMsg="Deleted Successfully",title="Patients Delete-HMS")
    else:
        return render_template("deleteDoctors.html",doctors=doctors,len=True if length!=0 else False ,error=True,errorMsg="You select nothing", success=False,successMsg=None,title="Patients Delete-HMS")    




@app.route('/patientMain')
def patientMain():
    global pname
    return render_template("patientMain.html",name = pname,title=f"{pname} Patient - HMS") 
 

@app.route('/newReport')
def newReport():   
    global pname
    return render_template('newReport.html', name = pname ,title="New Report - HMS",specializalitions=getModel().getSpecialization())  
  

@app.route('/latestReport')
def latestReport():
    global email
    global pname
    model = getModel()
    id = model.getPatientId(email)
    report=model.viewLatestReport(id)
    return render_template('latestReport.html',report=report,name=pname,len=False if report is None else True,title=f"{pname} Report")

@app.route('/myAllReports')
def myAllReports():
    global email
    global pname
    model = getModel()
    id = model.getPatientId(email)
    reports=model.myAllReports(id[0])
    return render_template('myAllReports.html' , reports=reports , name=pname , len=False if len(reports)==0 else True , title = f"{pname} Reports ")



@app.route('/showDoctors',methods=['post'])
def getSpectialization():
    model = getModel()
    global pname
    doctors = model.selectSpecializeDoctor(request.form["specialization"])
    return render_template('showDoctors.html',specilization=request.form["specialization"],doctors=doctors,len=True if doctors!=None else False ,name=pname,title=f"{pname} New-Appointment" ,msg="No Doctors")
    
    
#pending    
@app.route('/newAppointment')
def newAppointment():
    global pname
    model = getModel()
    specialization = model.getSpecialization()
    return render_template('newAppointment.html',specialization=specialization,len=True if specialization!=None else False ,name=pname,title=f"{pname} New-Appointment" ,msg="No Doctors")

@app.route('/finalizingReport', methods=['post'])
def finalizeAppointment():
    global pname,email
    model=getModel()
    pid = model.getPatientId(email)
    doc_id=request.form["doctors"]
    symptoms=request.form["symptoms"]
    statusDeal = model.addPatientDeal(pid[0], doc_id, symptoms)
    return render_template('patientMain.html',len=True if statusDeal!=None else False ,name=pname,title=f"{pname} Patient")
 

@app.route('/doctorMain')
def doctorMain():
    global pname
    return render_template('docMain.html',name=pname,title=f"Dr. {pname}-HMS")

curr=None
@app.route('/myCurrentPatient')
def myCurrentPatient():
    global pname
    global email,curr
    model = getModel()
    id = model.getDoctorId(email)
    print(id)
    curr = model.viewCurrentPatient(id)
    print(curr)
    return render_template("myCurrentPatient.html",curr=curr,name=pname,title="Current Patient",len=False if curr == None else True , msg="No Patients in a Queue.")



@app.route('/reportSubmit', methods=['post'])
def reportSubmit():
    global pname,email,curr
    model = getModel()
    model.updateDoctorDeal(curr[0],request.form["diagnosis"], request.form["fee"],request.form["medicines"])
    return redirect(url_for('myCurrentPatient'))
    
@app.route('/myWaitingPatients')
def waitingPatients():
    global pname,email,curr
    model = getModel()    
    patients = model.viewWaitingPatient(model.getDoctorId(email))
    return render_template("myWaitingPatients.html",patients=patients,name=pname,title="Waiting Patients-HMS",len=False if patients == None else True , msg="No Patients in a Waiting Queue.")
    
    
    
if __name__=='__main__':
    app.run(debug=True)