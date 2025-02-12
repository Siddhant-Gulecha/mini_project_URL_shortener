from flask import Flask, request, redirect, render_template
import sqlite3
import random
import string

app = Flask(__name__)
DATABASE = "urls.db"

# Function to create database table
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                long_url TEXT NOT NULL,
                short_url TEXT UNIQUE NOT NULL
            )
        """)
        conn.commit()

# Function to generate a random short URL
def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Route to display homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route to shorten URL
@app.route("/shorten", methods=["POST"])
def shorten_url():
    long_url = request.form["long_url"]
    short_url = generate_short_url()
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO urls (long_url, short_url) VALUES (?, ?)", (long_url, short_url))
        conn.commit()
    
    return f"Short URL: <a href='/r/{short_url}'>localhost:5000/r/{short_url}</a>"

# Route to redirect to original URL
@app.route("/r/<short_url>")
def redirect_url(short_url):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT long_url FROM urls WHERE short_url = ?", (short_url,))
        result = cursor.fetchone()
        
        if result:
            return redirect(result[0])
        else:
            return "URL not found", 404

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
