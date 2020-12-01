import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
db = sqlite3.connect("concerts.db", isolation_level=None)
db_cursor = db.cursor()

@app.route("/")
def Proeve():
    rows = db_cursor.execute("SELECT * FROM Koncert")
    return render_template("Proeve.html", rows=rows)