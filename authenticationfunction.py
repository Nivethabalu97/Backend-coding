import mysql.connector
def authentication(host,user,password):
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password)
    mycursor = mydb.cursor()
    return mycursor

value=authentication("host","root","Nivetha@123")
value.execute()