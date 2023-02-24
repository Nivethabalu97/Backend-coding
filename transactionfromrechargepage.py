import mysql.connector
from flask import Flask
from flask import request
from datetime import datetime

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
logger_log = logging.getLogger("Nivi")
logger_log.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler("login_details_"+currentdate+".log")
file_handler.setFormatter(formatter)
logger_log.addHandler(file_handler)


recharge_blueprint = Blueprint('recharge_blueprint', __name__)
mycursor = mydb.cursor()


@recharge_blueprint.route("/recharge", methods=["POST"])
def get_post_Request():

    amt = request.form.get("amount")
    amount = float(amt)
    transactiontype = request.form.get("transactiontype")
    loginid = request.form.get("loginid")
    current_time = datetime.now()
    status = True

    balance_record = f"SELECT balance FROM transactions WHERE loginid='nivetha' ORDER BY lastupdatedtime DESC"
    mycursor.execute(balance_record)
    bal_record = mycursor.fetchall()
    current_balance = bal_record[0][0]
    print(current_balance)
    new_balance = 0
    if transactiontype == "credit":
        new_balance = current_balance+amount
    else:
        new_balance = current_balance-amount
    print(type(new_balance))

    getData = {"loginid": loginid, "amount": amount,
               "transactiontype": transactiontype, "balance": new_balance, "status": status, "lastupdatedtime": current_time}
    print(getData)
    fields = ["loginid", "amount", "transactiontype",
              "balance", "status", "lastupdatedtime"]
    result = check_fields(fields, getData)
    if result["status"] == True:
        try:
            print("welcome world")
            count = "SELECT COUNT(loginid) FROM transactions WHERE loginid='nivetha'"
            mycursor.execute(count)
            myresult = mycursor.fetchone()
            print(len(myresult))
            if len(myresult) == 0 and getData["transactiontype"] == "credit" and getData["status"] == True:
                insert_query = "INSERT INTO transactions (loginid,amount,transactiontype,balance,status,lastupdatedtime) VALUES (%s,%f,%s,%f,%s,%s)"
                value_query = (getData["loginid"], getData["amount"], getData["transactiontype"], getData["balance"],
                               getData["status"], getData["lastupdatedtime"])
                mycursor.execute(insert_query, value_query)
                mydb.commit()
            elif len(myresult) == 0 and getData["transactiontype"] == "debit" and getData["status"] == True:
                print("Only credit type is allowed for first transaction")
            print("hello")
            if len(myresult) != 0 and current_balance > amount and getData["transactiontype"] == "debit" and getData["status"] == True:
                insert_query = "INSERT INTO transactions (loginid,amount,transactiontype,balance,status,lastupdatedtime) VALUES (%s,%f,%s,%f,%s,%s)"
                value_query = (getData["loginid"], getData["amount"], getData["transactiontype"], getData["balance"],
                               getData["status"], getData["lastupdatedtime"])
                mycursor.execute(insert_query, value_query)
                mydb.commit()
            elif (myresult) != 0 and current_balance > amount and getData["transactiontype"] == "credit" and getData["status"] == True:
                insert_query = "INSERT INTO transactions (loginid,amount,transactiontype,balance,status,lastupdatedtime) VALUES (%s,%f,%s,%f,%s,%s)"
                value_query = (getData["loginid"], getData["amount"], getData["transactiontype"], getData["balance"],
                               getData["status"], getData["lastupdatedtime"])
                mycursor.execute(insert_query, value_query)
                mydb.commit()
            elif (myresult) != 0 and current_balance < amount and getData["transactiontype"] == "credit" and getData["status"] == True:
                insert_query = "INSERT INTO transactions (loginid,amount,transactiontype,balance,status,lastupdatedtime) VALUES (%s,%f,%s,%f,%s,%s)"
                value_query = (getData["loginid"], getData["amount"], getData["transactiontype"], getData["balance"],
                               getData["status"], getData["lastupdatedtime"])
                mycursor.execute(insert_query, value_query)
                mydb.commit()
            elif (myresult) != 0 and current_balance < amount and getData["transactiontype"] == "debit" and getData["status"] == True:
                print("sorry insufficient balance")
            lastupdatedtime = getData["lastupdatedtime"]
            select_query = f"SELECT * FROM transactions where lastupdatedtime= {lastupdatedtime}"
            mycursor.execute(select_query)
            myresult = mycursor.fetchall()
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
        message = result["message"]
        logger.error(message)
        return message
