import sqlite3
from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__) #Create Flask app

@app.route("/") #Frontpage
def Frontpage(): #Define pop site#
    return render_template("Parent.html") #Return

@app.route("/pop") # Here we define which subpage the following code relates to
def pop(): #Define pop site#
    title = "Pop concerts"
    date = request.args.get('date') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect to database 
    rows = db_cursor.execute("SELECT * FROM concerts where genre='Pop' and Dato=?", (date,)) #Find the concerts matching the criteria genre, date, etc.
    return render_template("P7.html", rows=rows, title=title) #Return pop - her skal jeg undersøge hvordan man gør overskriften dynamisk 
    

@app.route("/jazz")
def Jazz(): #Define jazz site#
    title = "Jazz concerts"
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where genre='Jazz'") #Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/classic")
def Klassisk(): #Define classic site#
    title = "Classic concerts"
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where genre='Klassisk'") #Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/rock")
def Rock(): #Define rock site#
    title = "Rock concerts"
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where genre='Rock'") #Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/hiphop")
def Hiphop(): #Define hiphop site#
    title = "Hiphop concerts"
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where genre='Hiphop'") #Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/chosenConcert")
def chosenConcert(): 
    concertID = request.args.get('concertID') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect to database 
    rows = db_cursor.execute("SELECT * FROM concerts where Koncert_Id=?", (concertID,)) #Find the concerts matching the criteria genre, date, etc.
    return render_template("Concert.html", rows=rows) #Return pop - her skal jeg undersøge hvordan man gør overskriften dynamisk 
    
