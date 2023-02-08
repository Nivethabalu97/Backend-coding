from flask import Flask, render_template
from passwordcheck import login_blueprint
from signupapi import signup_blueprint
from storetransactionwitherrorhandling import store_blueprint
from sample import sample_blueprint
from Testing import testingbluePrint
from sam import sam_blueprint
from viewtransactions import viewtransaction_blueprint
from edittransaction import edit_blueprint

app = Flask(__name__)
app.register_blueprint(login_blueprint)
app.register_blueprint(signup_blueprint)
app.register_blueprint(store_blueprint)
app.register_blueprint(sample_blueprint)
app.register_blueprint(testingbluePrint)
app.register_blueprint(sam_blueprint)
app.register_blueprint(viewtransaction_blueprint)
app.register_blueprint(edit_blueprint)


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
