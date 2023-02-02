import mysql.connector
from flask import Flask
from flask import request
import datetime
import logging
from log import *

from flask import Blueprint
from genericfunctions import check_password, check_data_type, check_alphabets, check_mob_num, check_email, check_fields, currentdate


# app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nivetha@123",
    database="sampledatabase"
)

signup_blueprint = Blueprint('signup_blueprint', __name__)
mycursor = mydb.cursor()


@signup_blueprint.route("/signup", methods=["POST"])
def get_post_Request3():
    getData = request.json
    result_datatype = check_data_type(getData)
    result_alphabets = check_alphabets(getData)
    result_mobnumber = check_mob_num(getData)
    result_email = check_email(getData)
    result_password = check_password(getData)
    fields = ["firstname", "lastname", "emailid",
              "mobilenumber", "password", "dob"]
    result_fields = check_fields(fields, getData)
    id = generateid(getData)
    getData["id"] = id
    if result_datatype["status"] and result_alphabets["status"] and result_mobnumber["status"] and result_email["status"] and result_password["status"] and result_fields["status"] == True:
        try:

            signuptime = datetime.datetime.now()
            getData["signuptime"] = signuptime
            sql = "INSERT INTO signup (fname,lname,email,mobilenumber,password,dob,signuptime,id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (getData["firstname"], getData["lastname"], getData["emailid"], getData["mobilenumber"],
                   getData["password"], getData["dob"], getData["signuptime"], getData["id"])
            mycursor.execute(sql, val)
            mydb.commit()
            logger_log.info(id)
            filter = getData["password"]
            sql1 = "SELECT * FROM signup WHERE password='"+filter+"'"
            print(sql1)
            mycursor.execute(sql1)
            myresult = mycursor.fetchall()
            print(myresult)
            if (len(myresult)) != 0:
                message = "Successfully stored and status code: 200 "
                return message
            else:
                message = "Not Stored"
                logger.error(message)
                return message
        except TypeError as error:
            msg = "Sorry, invalid datatype" + str(error)
            logger.error(msg)
            return msg
        except Exception as error:
            message1 = "Sorry, your data cannot be stored in database" + \
                str(error)
            logger.error(message1)
            return message1
    else:
        logger.error("something wrong")
        return ("something went wrong"), "422"


def generateid(getData):
    fname = (getData["firstname"])
    name = ""
    for i in range(0, 4):
        name = name+fname[i]
    count = "000"
    name = name+"_"+count
    return name
