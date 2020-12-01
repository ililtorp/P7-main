#Flask code#
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pop(): #Define pop site#
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts") #Execute the concerts database
    return render_template("P7.html", rows=rows) #Return pop#
