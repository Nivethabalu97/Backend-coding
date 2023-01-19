import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nivetha@123",
  database="sampledatabase"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE transcations (tid INT AUTO_INCREMENT PRIMARY KEY, sno VARCHAR(255), date DATE,state VARCHAR(255),amount VARCHAR(255),transcationtype VARCHAR(255),balance VARCHAR(255),loginid VARCHAR(255),lastupdatedtime TIME)")
#mycursor.execute("SHOW TABLES")
#lisitng tables in db
#for x in mycursor:
  #print(x)
#mycursor.execute("ALTER TABLE transcations MODIFY COLUMN sno INT;")
#mycursor.execute("ALTER TABLE transcations RENAME TO transactions;")
mycursor.execute("ALTER TABLE transactions MODIFY COLUMN amount INT;")
#mycursor.execute("ALTER TABLE transactions MODIFY COLUMN balance INT;")