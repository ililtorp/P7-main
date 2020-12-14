import sqlite3
from flask import Flask, redirect, render_template, request
from datetime import datetime


app = Flask(__name__) #Create Flask app

@app.route("/") #Frontpage
def Frontpage(): #Define pop site#
    return render_template("Parent.html") #Return

@app.route("/pop") # Here we define which subpage the following code relates to
def pop(): 
    title = "Pop concerts"
    date = request.args.get('date') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect to database 
    rows = db_cursor.execute("SELECT * FROM concerts where Dato=? and Genre1='Pop' or Genre2='Pop'", (date,)) #Find the concerts matching the criteria 
    return render_template("P7.html", rows=rows, title=title) 
    

@app.route("/jazz")
def Jazz(): #Define jazz site#
    title = "Jazz concerts"
    date = request.args.get('date') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where Dato=? and Genre1='Jazz' or Genre2='Jazz'", (date,)) #Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/classic")
def Klassisk(): #Define classic site#
    title = "Classic concerts"
    date = request.args.get('date') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where Dato=? and Genre1='Klassisk' or Genre2='Klassisk'", (date,)) #Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/rock")
def Rock(): #Define rock site#
    title = "Rock concerts"
    date = request.args.get('date') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where Dato=? and Genre1='Rock' or Genre2='Rock'", (date,)) #Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/hiphop")
def Hiphop(): #Define hiphop site#
    title = "Hiphop concerts"
    date = request.args.get('date') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where Dato=? and Genre1='Hiphop' or Genre2='Hiphop'", (date,))#Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/metal")
def metal(): #Define hiphop site#
    title = "Metal concerts"
    date = request.args.get('date') #Gets the date from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where Dato=? and Genre1='Metal' or Genre2='Metal'", (date,))#Execute the concerts database
    return render_template("P7.html", rows=rows, title=title) #Return #

@app.route("/chosenConcert")
def chosenConcert(): 
    concertID = request.args.get('concertID') #Gets the concert id from the URL
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect to database 
    rows = db_cursor.execute("SELECT * FROM concerts where Koncert_Id=?", (concertID,)) #Find the concerts matching the concert ID
    return render_template("Concert.html", rows=rows) 

@app.route("/booking", methods=["GET", "POST"])
def booking(): 
    if request.method == "GET":
        concertID = request.args.get('concertID') #Gets the date from the URL
        db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
        db_cursor = db.cursor() #Connect to database 
        rows = db_cursor.execute("SELECT * FROM concerts where Koncert_Id=?", (concertID,)) #Find the concerts matching the concert ID
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
        return redirect("/confirmation?bookingID="+str(booking_ID)+"&ConcertID="+str(ConcertID)) 

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