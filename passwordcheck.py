import mysql.connector
from flask import Flask
from flask import request
import logging
from log import *
from datetime import date
from flask import Blueprint
from genericfunctions import check_password, currentdate


# app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nivetha@123",
    database="sampledatabase"
)
login_blueprint = Blueprint('login_blueprint', __name__)
mycursor = mydb.cursor()


# logging.basicConfig(filename="login_details.log", level=logging.INFO,
#                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')


@login_blueprint.route("/postLogin", methods=["POST"])
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
