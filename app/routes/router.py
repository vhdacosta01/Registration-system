from flask import Blueprint, render_template, request, redirect
from app.config.database import insert_user, login_attempt

from werkzeug.security import generate_password_hash

router = Blueprint("router", __name__)


@router.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        resultado = login_attempt(email, password)

        if resultado:
            return redirect("/dashboard")

    return render_template("login.html")


@router.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password, method="scrypt", salt_length=16)
        print("CHEGOU NO ROUTER:", name, email, hashed_password)

        insert_user(name, email, hashed_password)

    return render_template("register.html")


@router.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")