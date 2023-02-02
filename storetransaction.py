import mysql.connector
from flask import Flask, Blueprint
from flask import request
from genericfunctions import check_fields
from log import *


# app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nivetha@123",
    database="sampledatabase"
)
store_blueprint = Blueprint('store_blueprint', __name__)
mycursor = mydb.cursor()


@store_blueprint.route("/store", methods=["POST"])
def get_post_Request():
    getData = request.json
    d = check_fields(getData)
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
                message = "Successfully stored and status code 200 "
                logger_log.info(getData["loginid"])
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
        message = d["message"]
        logger.error(message)
        return message
