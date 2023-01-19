from flask import Flask
from flask import request

app = Flask(__name__)


# Here @app is a decorator
# www.google.com/
@app.route("/")
def hello_world():
    return "Hello world"
if __name__ == '__main__':
   app.run()