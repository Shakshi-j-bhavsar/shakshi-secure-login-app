"""
Secure Login Application
Developed by: Shakshi
Purpose: Demonstrate secure authentication & authorization
"""

from flask import Flask, render_template, request, redirect, session
from flask_bcrypt import Bcrypt
import psycopg2
import os
import secrets
secrets.token_hex(32)

from dotenv import load_dotenv
import os

load_dotenv()




app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


bcrypt = Bcrypt(app)

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax'
)

def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST")
    )

@app.route("/test")
def test():
    return "Flask server is running"

@app.route("/")
def home():
    return redirect("/login")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]

        if len(password) < 8:
            return "Password must be at least 8 characters"

        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, hashed_pw)
        )
        conn.commit()
        cur.close()
        conn.close()

        return redirect("/login")

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, password_hash, role FROM users WHERE email=%s",
            (email,)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and bcrypt.check_password_hash(user[1], password):
            session["user_id"] = user[0]
            session["role"] = user[2]
            return redirect("/dashboard")

        return "Invalid email or password"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

@app.route("/admin")
def admin():
    if "user_id" not in session or session.get("role") != "admin":
        return "Access denied"
    return render_template("admin.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True
    )


