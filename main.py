from flask import Flask, url_for, redirect, request, render_template
import login_singup_logic as lsl
import db_initialize as dbi
app = Flask(__name__)


@app.route("/")
def index():
    dbi.db_initilize()
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if lsl.main_login(email, password):
            return redirect(url_for("homepage"))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/singup", methods=["POST", "GET"])
def singup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        if lsl.sing_up(username, email, password):
            return redirect(url_for("login"))
        else:
            error = "one of the input fields is empty"
            return render_template("singup.html", error=error)
    else:
        return render_template("singup.html")


@app.route("/homepage")
def homepage():
    return render_template("home.html")
