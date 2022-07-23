import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices2"
) 

mycursor = db.cursor()



mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%S,%S)", ("Samuel Johsnson", " Ibuprofen", 20))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%S,%S)", ("Mathew Quinton"," Advil" , 40 ))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%S,%S)", ("Erham Bienga", " Ibuprofen", 30))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%S,%S)", ("Maxine Conti","Adrenaline ", 20 ))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%S,%S)", ("alexandra Anquilla","NAcamprosate tablets", 25  ))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%S,%S)", ("Adriana Tevez","Amantadine ", 30 ))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%S,%S)", ("Karen Mcvault", "Apomorphine", 51 ))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%S,%S)", ("Anthony Selvestor","Amisulpride ", 31 ))


mycursor.commit()