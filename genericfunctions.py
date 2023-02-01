from flask import Flask
import re
import logging
from datetime import date
currentdate = str(date.today())
# password check function


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

# string type check function


def check_data_type(getData: dict) -> dict:
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
# firstname and lastname alphabets check function


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
# mobile number check function


def check_mob_num(getData: dict) -> dict:
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
# email check function


def check_email(getData: dict) -> dict:
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
# check fields function


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
# error log configuration
