import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nivetha@123",
  database="sampledatabase"
)

mycursor = mydb.cursor()

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")
#mycursor.execute(sql, val)

#sql_1="INSERT INTO customers(name,address) VALUES (%s,%s)"
#val_1=("mike","dominick street 23")
#mycursor.execute(sql_1,val_1)

sql_2="INSERT INTO customers(name,address) VALUES (%s,%s)"
val_2=("jack","dominick lower street 22")
mycursor.execute(sql_2,val_2)

sql_3="INSERT INTO customers(name,address) VALUES (%s,%s)"
val_3=("mack","dominick upper street 21")
mycursor.execute(sql_3,val_3)


mydb.commit()

print(mycursor.rowcount, "record  successfully inserted.")