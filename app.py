from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("movies.sqlite")
    except sqlite3.Error as e:
        return conn

@app.route('/')
def hello():
    return "Hello World"

@app.route('/movies', methods=['GET', 'POST'])
def movies():    
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM movies")
        movies = [
            dict(id=row[0], title=row[1], released=row[2])
            for row in cursor.fetchall()
        ]
        if movies is not None:
            return jsonify(movies)
    
    if request.method == 'POST':
        new_title = request.form['title']
        new_released = request.form['released']
        sql = """INSERT INTO movies (title, released) VALUES (?, ?)"""
        cursor = cursor.execute(sql, (new_title, new_released))
        conn.commit()
        return f"Movie with the ID: {cursor.lastrowid} saved successfully", 201

if __name__ == '__name__':
    app.run()
