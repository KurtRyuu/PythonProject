import sqlite3

conn = sqlite3.connect("movies.sqlite")

cursor = conn.cursor()

sql_query = """ CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    released INTEGER NOT NULL
)"""

cursor.execute(sql_query)