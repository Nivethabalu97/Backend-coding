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
logger_log = logging.getLogger("Nivi")
logger_log.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler("login_details_"+currentdate+".log")
file_handler.setFormatter(formatter)
logger_log.addHandler(file_handler)

transaction_blueprint = Blueprint('transaction_blueprint', __name__)
mycursor = mydb.cursor()


@transaction_blueprint.route("/postUsers2", methods=["POST"])
def get_post_Request1():
    """
    This method will check for the certain conditions and will insert the data into sql database

    parameter: payload::<dict>
    return: response:: <dict>
    """
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

    if result_datatype["status"] and result_alphabets["status"] and result_mobilenumber["status"] and result_email["status"] and result_password["status"] and result_checkfields["status"] == True:
        try:
            signuptime = datetime.datetime.now()
            getData["signuptime"] = signuptime
            insert_query = f"INSERT INTO signup (fname,lname,email,mobilenumber,password,dob,signuptime,id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (getData["firstname"], getData["lastname"], getData["emailid"], getData["mobilenumber"],
                      getData["password"], getData["dob"], getData["signuptime"], getData["id"])
            mycursor.execute(insert_query, values)
            mydb.commit()
            search_filter = getData["id"]
            logger_log.info(search_filter)
            filter_query = "SELECT * FROM signup WHERE id='"+search_filter+"'"
            print(filter_query)
            mycursor.execute(filter_query)
            result = mycursor.fetchall()
            print(result)
            if (len(result)) != 0:
                message = "Successfully stored and status code: 200 "
                response = {"status": True, "message": message}
                return response
            else:
                message = "Not Stored"
                response = {"status": False, "message": message}
                logger.error(message)
                return response
        except TypeError as error:
            message = f"Sorry, invalid datatype because {error}"
            response = {"status": False, "message": message}
            logger.error(message)
            return response
        except Exception as error:
            message = f"Sorry, your data cannot be stored in database because {error}"
            response = {"status": False, "message": message}
            logger.error(message)
            return response
    elif result_datatype["status"] == False:
        logger.error(result_datatype["message"])
        return result_datatype, 422
    elif result_alphabets["status"] == False:
        logger.error(result_alphabets["message"])
        return result_alphabets, 422
    elif result_mobilenumber["status"] == False:
        logger.error(result_mobilenumber["message"])
        return result_mobilenumber, 422
    elif result_email["status"] == False:
        logger.error(result_email["message"])
        return result_email, 422
    elif result_password["status"] == False:
        logger.error(result_password["message"])
        return result_password, 422
    elif result_checkfields["status"] == False:
        logger.error(result_checkfields["message"])
        return result_checkfields, 422


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
