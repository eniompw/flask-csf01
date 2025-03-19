from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

con = sqlite3.connect("login.db")
cur = con.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(10) NOT NULL PRIMARY KEY,
                password VARCHAR(20) NOT NULL
            )''')
con.commit()
con.close()

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        return "signup success"
    
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if "bob" == request.form["username"] and \
            "123" == request.form["password"]:
            return "Hello " + request.form["username"]
        else:
            return "login failed"

if __name__ == "__main__":
    app.run(debug=True)