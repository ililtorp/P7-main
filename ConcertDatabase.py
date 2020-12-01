import csv
import sqlite3
import codecs

open("concerts.db", "w").close() #Husk databasen overskrives hver gang denne komando koeres

db = sqlite3.connect("concerts.db", isolation_level=None) #Connection to database, isolaiton level none is needed to directly perform queries on database
#db.text_factory = str #Needed to handle strings correctly on mac, not needed in CS50IDE
db_cursor = db.cursor()

db_cursor.execute("CREATE TABLE concerts (Koncert_id NUMERIC, Koncert TEXT, Beskrivelse TEXT, Spillested TEXT, Genre TEXT, Dato NUMERIC, Tid NUMERIC, Doerene_aabner TEXT, Varighed TEXT, Pris NUMERIC, Pladser TEXT)")

with open("concerts.csv", "r", encoding="utf-8") as importfile:
    reader = csv.DictReader(importfile, delimiter=",")
    for row in reader:
        Koncert_id = row["Koncert_ID"]
        Koncert = row["Koncert"]
        Beskrivelse = row["Beskrivelse af band"]
        Genre = row["Genre"]
        Spillested = row["Spillested"]
        Dato = row["Dato"]
        Tid = row["Tid"]
        Doerene_aabner = row["Doerene_aabner"]
        Varighed = row["Varighed"]
        Pris = row["Pris"]
        Pladser = row["Pladser"]
        db_cursor.execute("INSERT INTO concerts (Koncert_ID, Koncert, Beskrivelse, Spillested, Genre, Dato, Tid, Doerene_aabner, Varighed, Pris, Pladser) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                          (Koncert_id, Koncert, Beskrivelse, Spillested, Genre, Dato, Tid, Doerene_aabner, Varighed, Pris, Pladser))