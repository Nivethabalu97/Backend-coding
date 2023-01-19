import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nivetha@123",
  database="sampledatabase"
)
#variable name= predefined function
mycursor = mydb.cursor()
#create primary key while creating table itself
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#create primary key in existing table
mycursor.execute("ALTER TABLE customers ADD COLUMN  id INT AUTO_INCREMENT PRIMARY KEY")