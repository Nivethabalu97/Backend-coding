import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nivetha@123",
  database="sampledatabase"
)

mycursor = mydb.cursor()
#table creation
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
#lisitng tables in db
for x in mycursor:
  print(x)