import mysql.connector
from flask import Flask
from flask import request
import datetime
import re


app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nivetha@123",
    database="sampledatabase"
)

mycursor = mydb.cursor()


""" @app.route("/postUsers1", methods=["POST"])
def get_post_Request():
    getData = request.json
    d = check(getData)
    if d["status"] == True:
        try:
            sql = "INSERT INTO transactions (sno,entrydate,state,amount,transcationtype,balance,loginid,lastupdatedtime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (getData["sno"], getData["date"], getData["state"], getData["amount"],
                   getData["transcationtype"], getData["balance"], getData["loginid"], getData["lastupdatedtime"])
            mycursor.execute(sql, val)
            mydb.commit()
            filter = getData["sno"]
            sql1 = "SELECT * FROM transactions WHERE sno="+filter
            print(sql1)
            mycursor.execute(sql1)
            myresult = mycursor.fetchall()
            print(myresult)
            if (len(myresult)) != 0:
                message = "Successfully stored and status code: 201 "
                return message
            else:
                message = "Not Stored"
                return message
        except TypeError as error:
            msg = "Sorry, invalid datatype" + str(error)
            return msg
        except Exception as error:
            message1 = "Sorry, your data cannot be stored in database" + \
                str(error)
            return message1
    else:
        return d, "422"


def check(a):
    for i, j in a.items():
        if type(j) != str:
            print("please enter valid data")
            b = "datatype of " + str(i)+"is invalid"
            return {"status": False, "message": b}
        else:
            print("valid data")
    c = "all the data are valid type"
    return {"status": True, "message": c}
 """


@app.route("/postUsers2", methods=["POST"])
def get_post_Request1():
    getData = request.json
    d = check(getData)
    e = alpha(getData)
    f = num(getData)
    g = check1(getData)
    id = generateid(getData)
    getData["id"] = id
    if d and e and f and g == True:
        try:
            signuptime = datetime.datetime.now()
            getData["signuptime"] = signuptime
            sql = "INSERT INTO signup (fname,lname,email,mobilenumber,password,dob,signuptime,id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (getData["firstname"], getData["lastname"], getData["emailid"], getData["mobilenumber"],
                   getData["password"], getData["dob"], getData["signuptime"], getData["id"])
            mycursor.execute(sql, val)
            # mydb.commit()
            print("hai")
            filter = getData["id"]
            print("hello")
            sql1 = "SELECT * FROM transactions WHERE id="+filter
            print(sql1)
            mycursor.execute(sql1)
            myresult = mycursor.fetchall()
            print(myresult)
            if (len(myresult)) != 0:
                message = "Successfully stored and status code: 201 "
                return message
            else:
                message = "Not Stored"
                return message
        except TypeError as error:
            msg = "Sorry, invalid datatype" + str(error)
            return msg
        except Exception as error:
            message1 = "Sorry, your data cannot be stored in database" + \
                str(error)
            return message1
    else:
        note = "sorry try again"
        return note, "422"


def check(a):
    for i, j in a.items():
        if type(j) != str:
            print("please enter valid data")
            print("datatype of " + str(i)+"is invalid")
            b = False
            return b
        else:
            print("all the data are valid type")
            c = True
            return c


def generateid(getData):
    fname = (getData["firstname"])
    name = ""
    for i in range(0, 4):
        name = name+fname[i]
    count = "000"
    name = name+"_"+count
    return name


def alpha(getData):
    fname = (getData["firstname"])
    lname = (getData["lastname"])
    x = fname.isalpha()
    y = lname.isalpha()
    if x and y == True:
        z = True
        return z
    else:
        z = False
        return z


def num(getData):
    x = str(getData["mobilenumber"])
    y = (x.isdigit())
    if len(x) == 10 and y == True:
        z = True
        return z
    else:
        z = "mob number should be of strictly 10 digits and should not contain any alphabets"
        return z


def check1(getData):
    email = getData["emailid"]
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        z = True
        return z
    else:
        z = "Invalid Email"
        return z


if __name__ == '__main__':
    app.run()
