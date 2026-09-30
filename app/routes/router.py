from flask import Blueprint, render_template, request

router = Blueprint("router", __name__)


@router.route("/")
def login():
    return render_template("login.html")


@router.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        # sua lógica de cadastro ficará aqui
        pass

    return render_template("register.html")


@router.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")