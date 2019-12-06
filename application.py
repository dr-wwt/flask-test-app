import os
from flask import Flask
from flask import render_template, flash, redirect, url_for
from flask import send_file, send_from_directory


app = Flask(__name__)


@application.route('/')
@application.route('/index')
@application.route('/home')
def index():
    return render_template('index.html', title="Home")



@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Error"), 404


# if __name__ == "__main__":
#     app("0.0.0.0")
