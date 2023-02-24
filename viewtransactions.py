import mysql.connector
from flask import Flask
from flask import request
from log import *
from flask import Blueprint, render_template


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nivetha@123",
    database="sampledatabase"
)
viewtransaction_blueprint = Blueprint('viewtransaction_blueprint', __name__)
mycursor = mydb.cursor()


@viewtransaction_blueprint.route("/transactiondetails", methods=["GET"])
def get_transactions():
    head_query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'transactions'"
    mycursor.execute(head_query)
    res = mycursor.fetchall()
    print(res)
    new_heading = []
    for item in res:
        for j in item:
            new_item = f"{j}"
            new_heading.append(new_item.capitalize())
    print(new_heading)
    # new_list = [new_heading[7], new_heading[5], new_heading[2], new_heading[6],
    # new_heading[0], new_heading[8], new_heading[1], new_heading[4], new_heading[3]]

    sql_query = "SELECT * FROM transactions"
    mycursor.execute(sql_query)
    result = mycursor.fetchall()
    print(result)
    id_list = []
    for i in result:
        loginid = i[1]
        table_id = "id_"+loginid
        id_list.append(table_id)
    print(id_list)
    button_list = []
    for item in result:
        loginid = item[1]
        button_id = "000_"+loginid
        button_list.append(button_id)
    print(button_list)
    return render_template('t1.html', heading=new_heading, records=result, row_id=id_list, zip=zip, button_id=button_list)
