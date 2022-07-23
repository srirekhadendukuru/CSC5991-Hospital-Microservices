import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices2"
) 

mycursor = db.cursor()

mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Nick Advardo", 35, "8/1/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Tim Leoroy", 35, "8/1/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Colina Westwood", 40, "8/1/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Samuel Johsnson", 1804, " 1/23/23"))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Mathew Quinton", 1515, " 10/18/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Erham Bienga", 1706, " 12/17/23"))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Maxine Conti", 1107, "8/23/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("alexandra Anquilla", 1208,"8/26/22"  ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Adriana Tevez", 1290, "8/29/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Karen Mcvault", 1310, "9/13/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Anthony Selvestor", 1721, "12/13/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Anushka Kumail", 1522, "9/30/22"))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Juan Vaccino", 1920, "2/29/23"))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Megan Advardo", 1478, "10/17/22"))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%S,%S)", ("Olivia Tamina", 1560, "10/32/22"))

mycursor.commit()

