import mysql.connector
from flask import Flask
from flask import request
import re
import logging
from log import *
from datetime import date


app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nivetha@123",
    database="sampledatabase"
)

mycursor = mydb.cursor()
currentdate = str(date.today())

# logging.basicConfig(filename="login_details.log", level=logging.INFO,
#                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
logger_log = logging.getLogger("Nivi")
logger_log.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler("login_details_"+currentdate+".log")
file_handler.setFormatter(formatter)
logger_log.addHandler(file_handler)


@app.route("/postLogin", methods=["POST"])
def get_post_Request():
    """
    This method will check if the entered password
    matches with the any of the stored passwords in database 
    parameter: payload::<dict>
    return: response:: <dict>
    """
    getData = request.json
    result_checkpassword = check_password(getData)
    if result_checkpassword["status"] == True:
        try:
            password = getData["password"]
            print(password)
            # convert string datatype to tuple because sql query will return values in tuple datatype
            new_password = password,
            print(new_password)
            filter_query = "SELECT password FROM signup WHERE password='"+password+"'"
            print(filter_query)
            mycursor.execute(filter_query)
            result = mycursor.fetchone()
            print(result)
            if result == new_password:
                print("hello")
                message = "Login successfull "
                response = {"status": True, "message": message}
                user_query = "SELECT id FROM signup WHERE password='"+password+"'"
                print(user_query)
                mycursor.execute(user_query)
                user_id = mycursor.fetchone()
                print(user_id)
                logger_log.info(user_id)
                return response

            else:

                message = "Login failed! Please enter correct password"
                response = {"status": False, "message": message}
                logger.error(message)
                return response
        except Exception as error:
            message = f"Sorry, Login failed due to {error}"
            response = {"status": False, "message": message}
            logger.error(message)
            return response
    else:
        message = result_checkpassword["message"]
        logger.error(message)
        return result_checkpassword, "422"


def check_password(getData: dict) -> dict:
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
    elif len(password) < 8 and len(password) > 15:
        tip = "Password must be in length varies from 8 to 15 and must contain atleast one number,one uppercase and one lowercase letter and any one special character from (/?*&!@)"
        message = "Password length should be of minimum 8 and maximum of 15"
        response = {"status": False, "message": message, "tip": tip}
        return response
    elif password_alphanumeric == False:
        tip = "Password must be in length varies from 8 to 15 and must contain atleast one number,one uppercase and one lowercase letter and any one special character from (/?*&!@)"
        message = "Password should contain atleast one number"
        response = {"status": False, "message": message, "tip": tip}
        return response
    elif password_uppercase == False:
        tip = "Password must be in length varies from 8 to 15 and must contain atleast one number,one uppercase and one lowercase letter and any one special character from (/?*&!@)"
        message = "Password should contain atleast one uppercase letter"
        response = {"status": False, "message": message, "tip": tip}
        return response
    elif password_lowercase == False:
        tip = "Password must be in length varies from 8 to 15 and must contain atleast one number,one uppercase and one lowercase letter and any one special character from (/?*&!@)"
        message = "Password should contain atleast one lowercase letter"
        response = {"status": False, "message": message, "tip": tip}
        return response
    elif regex.search(password) == None:
        tip = "Password must be in length varies from 8 to 15 and must contain atleast one number,one uppercase and one lowercase letter and any one special character from (/?*&!@)"
        message = "Password should contain atleast one special character from (/?*&!@)"
        response = {"status": False, "message": message, "tip": tip}
        return response


if __name__ == '__main__':
    app.run()
