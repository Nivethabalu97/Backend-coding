from flask import Flask
from flask import request

app = Flask(__name__)



@app.route("/postUsers", methods=["POST"])
def get_post_Request():
    getData = request.json
    return getData

if __name__ == '__main__':
   app.run()