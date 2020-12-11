import sqlite3
from flask import Flask, redirect, render_template, request
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
    rows = db_cursor.execute("SELECT * FROM concerts where Genre1='Pop'and Dato=?", (date,)) #Find the concerts matching the criteria genre, date, etc.
    return render_template("P7.html", rows=rows, title=title) #Return pop - her skal jeg undersøge hvordan man gør overskriften dynamisk 
    

@app.route("/jazz")
def Jazz(): #Define jazz site#
    title = "Jazz concerts"
    date = request.args.get('date') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where Genre1='Jazz'and Dato=?", (date,)) #Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/classic")
def Klassisk(): #Define classic site#
    title = "Classic concerts"
    date = request.args.get('date') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where Genre1='Klassisk'and Dato=?", (date,)) #Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/rock")
def Rock(): #Define rock site#
    title = "Rock concerts"
    date = request.args.get('date') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where Genre1='Rock'and Dato=?", (date,)) #Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/hiphop")
def Hiphop(): #Define hiphop site#
    title = "Hiphop concerts"
    date = request.args.get('date') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where Genre1='Hiphop'and Dato=?", (date,)) #Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/chosenConcert")
def chosenConcert(): 
    concertID = request.args.get('concertID') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect to database 
    rows = db_cursor.execute("SELECT * FROM concerts where Koncert_Id=?", (concertID,)) #Find the concerts matching the criteria genre, date, etc.
    return render_template("Concert.html", rows=rows) #Return pop - her skal jeg undersøge hvordan man gør overskriften dynamisk 

@app.route("/booking", methods=["GET", "POST"])
def booking(): 
    if request.method == "GET":
        concertID = request.args.get('concertID') #Gets the date from the URL
        db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
        db_cursor = db.cursor() #Connect to database 
        rows = db_cursor.execute("SELECT * FROM concerts where Koncert_Id=?", (concertID,)) #Find the concerts matching the criteria genre, date, etc.
        return render_template("booking.html", rows=rows) #Return booking.html - redirects to the booking page
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        ConcertID = request.form.get("ConcertID")
        NTickets = request.form.get("NTickets")
        db = sqlite3.connect("kunder.db", isolation_level=None) #Connect database to HTML
        db_cursor = db.cursor() #Connect to database 
        db_cursor.execute("INSERT INTO kundedata (name, email, phone, ConcertID, NTickets) VALUES (?, ?, ?, ?, ?)", (name, email, phone, ConcertID, NTickets))
        booking_ID = db_cursor.lastrowid
        return redirect("/confirmation?bookingID="+str(booking_ID)+"&ConcertID="+str(ConcertID)) #Her skal vi lave et link, til når man succesfuldt har booket sin billet. 

@app.route("/confirmation")
def confirmation():
    booking_ID = request.args.get('bookingID')
    concertID = request.args.get('ConcertID')
    kunde_db = sqlite3.connect("kunder.db", isolation_level=None) #Connect database to HTML
    kunde_db_cursor = kunde_db.cursor() #Connect to database
    rows = kunde_db_cursor.execute("SELECT * FROM kundedata where id=?", (booking_ID,))
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect to database 
    concert = db_cursor.execute("SELECT * FROM concerts where Koncert_Id=?", (concertID,))
    return render_template("billet.html", rows=rows, concert=concert)