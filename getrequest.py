from flask import Flask
from flask import request

app = Flask(__name__)



@app.route("/getusers", methods=["GET"])
def get_users():
    return {"user1": "nivetha"}

if __name__ == '__main__':
   app.run()