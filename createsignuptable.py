import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nivetha@123",
  database="sampledatabase"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE signup(sno INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255),lname VARCHAR(255),email NVARCHAR(320),password VARCHAR(255),dob DATE,signuptime TIMESTAMP,id VARCHAR(255))")
#mycursor.execute("SHOW TABLES")
#mycursor.execute("ALTER TABLE signup ADD COLUMN mobilenumber INT;")
mycursor.execute("ALTER TABLE signup MODIFY COLUMN signuptime DATETIME;")