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
    result_datatype = check_data_type(getData)
    e = alpha(getData)
    f = num(getData)
    g = check1(getData)
    h=password_check(getData)
    fields=["firstname","lastname","emailid","mobilenumber","password","dob"]
    i=check_fields(fields,getData)
    id = generate_id(getData)
    getData["id"] = id
    if result_datatype["status"] and e["status"] and f["status"] and g["status"] and h["status"] and i["status"]== True:
        try:
            signuptime = datetime.datetime.now()
            getData["signuptime"] = signuptime
            sql = "INSERT INTO signup (fname,lname,email,mobilenumber,password,dob,signuptime,id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (getData["firstname"], getData["lastname"], getData["emailid"], getData["mobilenumber"],
                   getData["password"], getData["dob"], getData["signuptime"], getData["id"])
            mycursor.execute(sql, val)
            mydb.commit()
            print("hai")
            filter = getData["id"]
            print("hello")
            sql1 = "SELECT * FROM signup WHERE id='"+filter+"'"
            print(sql1)
            mycursor.execute(sql1)
            myresult = mycursor.fetchall()
            print(myresult)
            if (len(myresult)) != 0:
                message = "Successfully stored and status code: 200 "
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
    elif result_datatype["status"]==False:
        return result_datatype,422
    elif e["status"]==False:
        return e,422
    elif f["status"]==False:
        return f,422
    elif g["status"]==False:
        return g,422
    elif h["status"]==False:
        return h,422
    elif i["status"]==False:
        return i,422

def check_data_type(getData: dict):
    """
    This method will check if the given values
    in the dictionary is string or not

    parameter: payload::<dict>
    return: response:: <dict>
    """
    for keys, values in getData.items():
        if type(values) != str:
            message=f"Datatype of {keys} is invalid"
            response= {"status":False,"message":message}
            return response
        else:
            message = "All the data are valid type"
            response={"status":True,"message":message}
    return response


def generate_id(getData:dict):
    """
    This method will generate unique id for every user 
    based on the firstname of the user 
    
    parameter: payload::<dict>
    return: new_id:: <string>
    """
    first_name = (getData["firstname"])
    new_id = ""
    for alphabet in range(0, 4):
        new_id = new_id+first_name[alphabet]
    count = "000"
    new_id = new_id+"_"+count
    return new_id


def alpha(getData):
    fname = (getData["firstname"])
    lname = (getData["lastname"])
    x = fname.isalpha()
    y = lname.isalpha()
    if x and y == True:
        z = True
        return {"status":True}
    else:
        m1="firstname and lastname should not contain any numbers"
        z = False
        return {"status":False,"message":m1}


def num(getData):
    x = getData["mobilenumber"]
    y = (getData["mobilenumber"].isdigit())
   
    if len(x) == 10 and y == True:
        z = True
        return {"status":True}
    else:
        m1 = "mob number should be of strictly 10 digits and should not contain any alphabets"
        return {"status":False,"message":m1}


def check1(getData):
    email = getData["emailid"]
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        return{"status":True}
    else:
        m1="email id should be of correct format"
        return{"status":False,"message":m1}

# def check_fields(listOfFields, _dictionary):
#     """
#     This method should check if the give fields are
#     available in the dictionary or not
#     Eg - ["fname", "lname", "dob"]
#     Check if these keys are present in the _dictionary
#     """

# def check_password(password):
#     """
#     This method will do the following checks
#     - If the password is in the range of length 8-15
#     - If the passsword has atleast one number
#     - If the password has atleast one Capital letter
#     - If the password has atleast one small letter
#     - If the password has atleast one special character from /?*&!
#     """

# Commit history order
# - Write the password method - Not tested
# - Tested code
# - write check fields - Not tested
# - Tested code
# - For each foramtted and documented function, a commit should be done

def password_check(getData):
    x=getData["password"]
    #number check
    y=bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', x))
    #uppercase check
    z= bool(re.match(r'\w*[A-Z]\w*', x))
    #lowercase check
    z1=bool(re.match(r'\w*[a-z]\w*', x))
    #special character check
    regex = re.compile('[/?*&!@]')
    z2=getData["password"]
    
    if len(x) >=8 and len(x)<=15 and y==True and z==True and z1==True and regex.search(z2) != None:
        response={"status":True}
        return response
        
    else:
        response={"status":False,"message":"Password must be in length varies from 8 to 15 and must contain atleast one number,one uppercase and one lowercase letter and any one special character from (/?*&!@)"} 
        return response

def check_fields(fields,getData):
    for i in fields:
        for j in getData.keys():
            if i ==j :
                a=True
            else:
                a=False
    
    if a==True:
        response={"status":True,"message":"success"}
        return response
    else:
        response={"status":False,"message":"Please enter all required fields"}
        return response


if __name__ == '__main__':
    app.run()
