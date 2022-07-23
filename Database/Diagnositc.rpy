import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices2"
) 

mycursor = db.cursor()

mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Nick Advardo", 101, "X-Ray" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Tim Leoroy", 102, "X-Ray" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Colina Westwood", 103, "Ultra-Sound" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Samuel Johsnson", 101, " X-Ray"))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Mathew Quinton", 102, " X-Ray" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Erham Bienga", 103, " Ultra-Sound"))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Maxine Conti", 103, "Ultra-Sound" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("alexandra Anquilla", 103,"Ultra-Sound"  ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Adriana Tevez", 103, "Ultra-Sound" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Karen Mcvault", 103, "Ultra-Sound" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Anthony Selvestor", 102, "X-Ray" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Anushka Kumail", 101, "X-Ray"))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Juan Vaccino", 102, "X-Ray"))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Megan Advardo", 101, "X-Ray"))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%S,%S)", ("Olivia Tamina", 103, "Ultra-Sound"))

mycursor.commit()

