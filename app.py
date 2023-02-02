from flask import Flask, render_template
from passwordcheck import login_blueprint
from signupapi import signup_blueprint
from storetransactionwitherrorhandling import transaction_blueprint
from sample import sample_blueprint
from storetransaction import store_blueprint
from sam import sam_blueprint

app = Flask(__name__)
app.register_blueprint(login_blueprint)
app.register_blueprint(signup_blueprint)
app.register_blueprint(transaction_blueprint)
app.register_blueprint(sample_blueprint)
app.register_blueprint(store_blueprint)
app.register_blueprint(sam_blueprint)


if __name__ == '__main__':
    app.run()
