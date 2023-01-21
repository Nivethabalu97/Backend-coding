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
    result_alphabets = check_alphabets(getData)
    result_mobilenumber = check_mob_num(getData)
    result_email = check_email(getData)
    result_password = check_password(getData)
    fields = ["firstname", "lastname", "emailid",
              "mobilenumber", "password", "dob"]
    result_checkfields = check_fields(fields, getData)
    id = generate_id(getData)
    getData["id"] = id
    result_password = check_password(getData)
    if result_datatype["status"] and result_alphabets["status"] and result_mobilenumber["status"] and result_email["status"] and result_password["status"] and result_checkfields["status"] == True:
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
    elif result_datatype["status"] == False:
        return result_datatype, 422
    elif result_alphabets["status"] == False:
        return result_alphabets, 422
    elif result_mobilenumber["status"] == False:
        return result_mobilenumber, 422
    elif result_email["status"] == False:
        return result_email, 422
    elif result_password["status"] == False:
        return result_password, 422
    elif result_checkfields["status"] == False:
        return result_checkfields, 422


def check_data_type(getData: dict):
    """
    This method will check if the given values
    in the dictionary is string or not

    parameter: payload::<dict>
    return: response:: <dict>
    """
    for keys, values in getData.items():
        if type(values) != str:
            message = f"Datatype of {keys} is invalid"
            response = {"status": False, "message": message}
            return response
        else:
            message = "All the data are valid type"
            response = {"status": True, "message": message}
    return response


def generate_id(getData: dict):
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


def check_alphabets(getData):
    """
    This method will check if the firstname and lastname
    of the user contains only alphabets

    parameter: payload::<dict>
    return: response:: <dict>
    """
    first_name = (getData["firstname"])
    last_name = (getData["lastname"])
    result_firstname = first_name.isalpha()
    result_lastname = last_name.isalpha()
    if result_firstname and result_lastname == True:
        message = "Valid firstname and lastname"
        response = {"status": True, "message": message}
        return response
    else:
        message = "firstname and lastname should not contain any numbers"
        response = {"status": False, "message": message}
        return response


def check_mob_num(getData):
    """
    This method will check if the given mobilenumber
    of the user contains only digits

    parameter: payload::<dict>
    return: response:: <dict>
    """
    mob_number = getData["mobilenumber"]
    result_mobnumber = (getData["mobilenumber"].isdigit())

    if len(mob_number) == 10 and result_mobnumber == True:
        message = "valid mobile number"
        response = {"status": True, "message": message}
        return response
    else:
        message = "mob number should be of strictly 10 digits and should not contain any alphabets"
        response = {"status": False, "message": message}
        return response


def check_email(getData):
    """
    This method will check if the given emailid
    is in correct format

    parameter: payload::<dict>
    return: response:: <dict>
    """
    email = getData["emailid"]
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        message = "valid emailid"
        response = {"status": True, "message": message}
        return response
    else:
        message = "email id should be of correct format"
        response = {"status": False, "message": message}
        return response

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


def check_password(getData):
    """
    This method will check if the entered password 
    is in correct format

    parameter: payload::<dict>
    return: response:: <dict>
    """
    password = getData["password"]
    # number check
    password_alphanumeric = bool(
        re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', password))
    # uppercase check
    password_uppercase = bool(re.match(r'\w*[A-Z]\w*', password))
    # lowercase check
    password_lowercase = bool(re.match(r'\w*[a-z]\w*', password))
    # special character check
    regex = re.compile('[/?*&!@]')

    if len(password) >= 8 and len(password) <= 15 and password_alphanumeric == True and password_uppercase == True and password_lowercase == True and regex.search(password) != None:
        message = "Strong Password"
        response = {"status": True, "message": message}
        return response

    else:
        message = "Password must be in length varies from 8 to 15 and must contain atleast one number,one uppercase and one lowercase letter and any one special character from (/?*&!@)"
        response = {"status": False, "message": message}
        return response


def check_fields(fields, getData):
    """
    This method will check the keys of the payload dict with list of fields.

    parameter: payload::<dict>
    return: response:: <dict>
    """
    for elements in fields:
        for keys in getData.keys():
            if elements == keys:
                result_compare = True
            else:
                result_compare = False

    if result_compare == True:
        message = "success"
        response = {"status": True, "message": message}
        return response
    else:
        message = "Please enter all required fields"
        response = {"status": False, "message": message}
        return response


if __name__ == '__main__':
    app.run()
