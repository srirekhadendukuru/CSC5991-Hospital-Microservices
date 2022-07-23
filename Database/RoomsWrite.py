import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices2"
) 

mycursor = db.cursor()

mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Nick Advardo", 101, "X-Ray" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Tim Leoroy", 102, "X-Ray" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Colina Westwood", 103, "Ultra-Sound" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Samuel Johsnson", 104, " Surgery"))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Mathew Quinton", 105, " Surgery" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Erham Bienga", 106, " Surgery"))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Maxine Conti", 107, "Neurology" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("alexandra Anquilla", 108,"Neurology"  ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Adriana Tevez", 109, "Neurology" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Karen Mcvault", 110, "Neurology" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Anthony Selvestor", 111, "Neurology" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Anushka Kumail", 112, "Emergency Room"))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Juan Vaccino", 113, "Emergency Room"))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Megan Advardo", 114, "Emergency Room"))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%S,%S)", ("Olivia Tamina", 115, "Emergency Room"))

mycursor.commit()

