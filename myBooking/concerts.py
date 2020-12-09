import sqlite3
from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__) #Create Flask app

@app.route("/mytickets")
def mytickets():
    return render_template("mytickets.html")