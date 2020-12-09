import csv
import sqlite3
import codecs

open("concerts.db", "w").close() #Husk databasen overskrives hver gang denne komando koeres

db = sqlite3.connect("concerts.db", isolation_level=None) #Connection to database, isolaiton level none is needed to directly perform queries on database
db.text_factory = str #Needed to handle strings correctly on mac, not needed in CS50IDE
db_cursor = db.cursor()

db_cursor.execute("CREATE TABLE concerts (Koncert_ID NUMERIC, Koncert TEXT, Beskrivelse TEXT, Spillested TEXT, Genre1 TEXT, Genre2 TEXT, Dato NUMERIC, Tid NUMERIC, Doerene_aabner TEXT, Varighed TEXT, Pris NUMERIC, Pladser TEXT, Billede IMAGE)")

with open("concerts.csv", "r", encoding="utf-8") as importfile:
    reader = csv.DictReader(importfile, delimiter=",")
    for row in reader:
        Koncert_ID = row["Koncert_ID"]
        Koncert = row["Koncert"]
        Beskrivelse = row["Beskrivelse"]
        Genre1 = row["Genre1"]
        Genre2 = row["Genre2"]
        Spillested = row["Spillested"]
        Dato = row["Dato"]
        Tid = row["Tid"]
        Doerene_aabner = row["Doerene_aabner"]
        Varighed = row["Varighed"]
        Pris = row["Pris"]
        Pladser = row["Pladser"]
        Billede = row["Billede"]
        db_cursor.execute("INSERT INTO concerts (Koncert_ID, Koncert, Beskrivelse, Spillested, Genre1, Genre2, Dato, Tid, Doerene_aabner, Varighed, Pris, Pladser, Billede) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                          (Koncert_ID, Koncert, Beskrivelse, Spillested, Genre1, Genre2, Dato, Tid, Doerene_aabner, Varighed, Pris, Pladser, Billede))