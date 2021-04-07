"""dababy."""
from flask import Flask, redirect, url_for, render_template, request, session, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from .init import user_collection

user = Blueprint('user', __name__, url_prefix='/user')

@user.route("/login", methods=["GET", "POST"])
def login():
    """hello."""
    if request.method == "POST":
        session.pop("email", None)
        email = request.form["email"]
        password = request.form["password"]

        user = user_collection.find_one({"email": email})
        if user and check_password_hash(user["password"], password):
            session["email"] = user["email"]
            return redirect("/")
        else:
            flash("Incorrect username or password.")
            return redirect("/user/login")
    else:
        return render_template("login.html")


@user.route("/register", methods=["GET", "POST"])
def register():
    """hello."""
    if request.method == "POST":
        # check if email is in use
        email = request.form["email"]
        user = user_collection.find_one({"email": email})
        if user:
            flash("Unfortunately, that email is in use. Please try again.")
            return redirect("/user/register")

        # confirm password and hash
        password = request.form["password"]
        cpassword = request.form["cpassword"]
        if password != cpassword:
            flash("Your passwords did not match.")
            return redirect("/user/register")
        hashed_password = generate_password_hash(password, method="sha256")

        name = request.form["name"]
        
        # post user to database
        post = {
            "email": email,
            "password": hashed_password,
            "name": name,
            "necrotic_wake": {
                "plus0T": 0,
                "plus1T": 0,
                "plus2T": 0,
                "plus3T": 0,
                "plus4T": 0,
                "plus5T": 0,
                "plus6T": 0,
                "plus7T": 0,
                "plus8T": 0,
                "plus9T": 0,
                "plus10T": 0,
                "plus0": 0,
                "plus1": 0,
                "plus2": 0,
                "plus3": 0,
                "plus4": 0,
                "plus5": 0,
                "plus6": 0,
                "plus7": 0,
                "plus8": 0,
                "plus9": 0,
                "plus10": 0
            },
        }
        user_collection.insert_one(post)
        flash("Your account was successfully made! Please login now.")
        return redirect("/user/login")
    else:
        return render_template("register.html")
    
    
@user.route("/sign-out", methods=["GET"])
def sign_out():
    """hello."""
    session.pop("email", None)
    return redirect("/user/login")