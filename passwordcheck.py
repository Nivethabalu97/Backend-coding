import mysql.connector
from flask import Flask
from flask import request
import re
import logging
from datetime import date


app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nivetha@123",
    database="sampledatabase"
)

mycursor = mydb.cursor()
currentdate = date.today()
logging.basicConfig(
    filename=f"api_debug_{currentdate}.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


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
                message = "Login successfull "
                response = {"status": True, "message": message}
                user_query = "SELECT id FROM signup WHERE password='"+password+"'"
                print(user_query)
                mycursor.execute(user_query)
                user_id = mycursor.fetchone()
                print(user_id)
                logger.info(user_id)
                return response
            else:
                message = "Login failed! Please enter correct password"
                response = {"status": False, "message": message}
                return response
        except Exception as error:
            message = f"Sorry, Login failed due to {error}"
            response = {"status": False, "message": message}
            return response
    else:
        logger.error(result_checkpassword)
        return result_checkpassword, "422"


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


if __name__ == '__main__':
    app.run()
