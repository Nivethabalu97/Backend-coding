import mysql.connector
from flask import Flask
from flask import request
from log import *
from flask import Blueprint,render_template

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nivetha@123",
    database="sampledatabase"
)
edit_blueprint = Blueprint('edit_blueprint', __name__)
mycursor = mydb.cursor()



@edit_blueprint.route("/edit", methods=["GET"])
def view_transaction():
    tid_values=request.args.get('tid')
    sno_values=request.args.get('sno')
    entrydate_values=request.args.get('entrydate')
    state_values=request.args.get('state')
    amount_values=request.args.get('amount')
    transactiontype_values=request.args.get('transactiontype')
    balance_values=request.args.get('balance')
    loginid_values=request.args.get('loginid')
    time_values=request.args.get('lastupdatedtime')
    values=[tid_values,sno_values,entrydate_values,state_values,amount_values,transactiontype_values,balance_values,loginid_values,time_values]
    print(values)
    label_names=["Transaction id","Sno","Entry Date","State","Amount","Transaction Type","Balance","Loginid","Lastupdated Time"]
    
    return render_template('form.html', pagetitle='edit form',output=values,labels_list=label_names,zip=zip)
    


    
    

