import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices2"
) 

mycursor = db.cursor()


mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%S,%S)", ("Samuel Johsnson", "Broken Right Ankle", " Surgery"))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%S,%S)", ("Mathew Quinton", "Broken Left Sholder ", " Surgery" ))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%S,%S)", ("Erham Bienga", "Broken Tibia", " Surgery"))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%S,%S)", ("Maxine Conti", "Brain Tumor", "Neurology" ))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%S,%S)", ("alexandra Anquilla", "Leg Paralisis","Neurology"  ))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%S,%S)", ("Adriana Tevez", "Brain Contusion", "Neurology" ))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%S,%S)", ("Karen Mcvault", "Brain Cancer", "Neurology" ))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%S,%S)", ("Anthony Selvestor", "Brain Contusion", "Neurology" ))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%S,%S)", ("Anushka Kumail", "Heart Attack", "Emergency Room"))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%S,%S)", ("Juan Vaccino", "Severe Brain Contution", "Emergency Room"))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%S,%S)", ("Megan Advardo", "Punctured Lung", "Emergency Room"))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%S,%S)", ("Olivia Tamina", "Neck Fracture", "Emergency Room"))

mycursor.commit()
