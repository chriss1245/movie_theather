from flask import Blueprint, redirect, url_for, render_template, request, flash
from . import model, bcrypt, db
import flask_login

bp = Blueprint("auth", __name__)


# ----------------------LOGIN--------------------------------------
@bp.route("/login")
def login():
    return render_template("main/login.html")


@bp.route("/login", methods=["POST"])
def post_login():
    email = request.form.get("email")
    password = request.form.get("password")

    user = model.User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        flask_login.login_user(user)
        return redirect(url_for("main.home"))
    flash("Wrong email or password. Try again")
    return redirect(url_for("auth.login"))


# -----------------------SIGNUP--------------------------------------
@bp.route("/register")
def register():
    return render_template("main/register.html")


@bp.route("/register", methods=["POST"])
def post_register():
    email = request.form.get("email")
    username = request.form.get("name")
    password = request.form.get("password")

    # Equal passwor/singup/singupds
    if password != request.form.get("password_repeat"):
        flash("Passwords differ")
        return redirect(url_for("auth.register"))

    # Check if the email is already at the database
    user = model.User.query.filter_by(email=email).first()
    if user:
        flash("User already exists")
        return redirect(url_for("auth.register"))

    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = model.User(
        email=email, name=username, password=password_hash, admin=False
    )

    db.session.add(new_user)
    db.session.commit()
    flask_login.login_user(new_user)
    return redirect(url_for("main.user_template"))


# -------------------------LOGOUT---------------------------------------
@bp.route("/logout")
def logout():
    flask_login.logout_user()
    return redirect(url_for("main.home"))
