import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nivetha@123"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE sampledatabase")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)