from flask import Flask
from flask import request

app = Flask(__name__)



@app.route("/getusers2/<userName>", methods=["GET"])
def get_users_by_request(userName):
    usernames = {"abhishek": "50", "nivi": "30"}
    if userName not in usernames:
        return "Given " + userName + " Not found"
    return usernames[userName]

if __name__ == '__main__':
   app.run()