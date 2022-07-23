import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices2"
) 

mycursor = db.cursor()

mycursor.execute("INSERT INTO Doctor (DOCname, DOCphone, DOCfield,  DOCdaysPresent, DOCtimePresent) VALUES (%s,%S,%S, %S, %S)", ("Dr. Richmond", 5866673243, "Neurologists", "Monday-Friday", "8:00am - 4:00 pm"))
mycursor.execute("INSERT INTO Doctor (DOCname, DOCphone, DOCfield,  DOCdaysPresent, DOCtimePresent) VALUES (%s,%S,%S, %S, %S)", ("Dr. Patel", 5869723456, "Radiologists", "Monday-Friday", "10:00am - 6:00 pm"))
mycursor.execute("INSERT INTO Doctor (DOCname,  DOCphone, DOCfield,  DOCdaysPresent, DOCtimePresent) VALUES (%s,%S,%S, %S, %S)", ("Dr. Westwood", 5869601234, "Emergency Medicine Specialists", "Wednessday-Saturday", "6:00am - 2:00 pm"))
mycursor.execute("INSERT INTO Doctor (DOCname,  DOCphone, DOCfield,  DOCdaysPresent, DOCtimePresent) VALUES (%s,%S,%S, %S, %S)", ("Dr. Alexis", 586031295, "Orthopedic", "Wednessday-Saturday", "8:00pm - 4:00 am"))
mycursor.execute("INSERT INTO Doctor (DOCname, DOCphone, DOCfield,  DOCdaysPresent, DOCtimePresent) VALUES (%s,%S,%S, %S, %S)", ("Dr. Asumeng", 5867623456, "Internists", "Monday-Friday", "12:00pm - 8:00 pm"))
mycursor.execute("INSERT INTO Doctor (DOCname,  DOCphone, DOCfield,  DOCdaysPresent, DOCtimePresent) VALUES (%s,%S,%S, %S, %S)", ("Dr. Richardo", 5863245098, "Oncologists", "Monday-Friday", "11:00am - 7:00 pm"))


mycursor.commit()

