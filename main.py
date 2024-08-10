from flask import Flask, url_for, redirect, request, render_template, session
import login_singup_logic as lsl
import db_initialize as dbi
import secret

app = Flask(__name__)

app.secret_key = secret.SECRET_KEY


@app.route("/")
def index():
    dbi.db_initilize()
    if 'username' in session:
        return redirect(url_for("homepage"))
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if lsl.main_login(email, password):
            session['username'] = lsl.get_username(email)
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
    if 'username' in session:
        return render_template("home.html", username=session['username'])
    else:
        return redirect(url_for('login'))


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for("index"))
