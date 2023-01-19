import mysql.connector
from flask import Flask
from flask import request
from datetime import datetime

app = Flask(__name__)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nivetha@123",
  database="sampledatabase"
)

mycursor = mydb.cursor()
@app.route("/postUsers", methods=["POST"])
def get_post_Request():
    getData = request.json
    #x=getData["date"]
    #format = "%m/%d/%Y"
    #x1 = datetime.strptime(x, format)
    #y=getData["lastupdatedtime"]
    #format1="%H:%M%p"
    #y1=datetime.strptime(y, format1)
    #getData["date"] = x1
    #getData["lastupdatedtime"] = y1
    sql = "INSERT INTO transactions (sno,entrydate,state,amount,transcationtype,balance,loginid,lastupdatedtime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (getData["sno"],getData["date"],getData["state"],getData["amount"],getData["transcationtype"],getData["balance"],getData["loginid"],getData["lastupdatedtime"])
    mycursor.execute(sql, val)
    mydb.commit()
    message="Successfully stored in database"
    return message


print(mycursor.rowcount, "record  successfully inserted.")


if __name__ == '__main__':
   app.run()