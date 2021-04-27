"""dababy."""
from flask import Flask, redirect, url_for, render_template, request, session, flash, Blueprint, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .init import user_collection
from .init import assignment_collection

user = Blueprint('user', __name__, url_prefix='/user')


@user.route("/get_student", methods=["GET"])
def get_user():
    user = user_collection.find_one({"email": request.args["studentEmail"]})
    return jsonify(
        email=user["email"],
        name=user["name"],
        coins=user["coins"]
    )


@user.route("/login", methods=["GET", "POST"])
def login():
    """hello."""
    if request.method == "POST":
        session.pop("email", None)
        email = request.form["email"]
        password = request.form["password"]

        user = user_collection.find_one({"email": email})
        if user["type"] == "Student":
            flash(
                "Tried to login with a student account. This login is only for teachers.")
            return redirect("/user/login")
        elif user and check_password_hash(user["password"], password):
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
        accountType = request.form["type"]

        # create post
        post = {
            "email": email,
            "password": hashed_password,
            "name": name,
            "type": accountType,
        }

        if accountType == "Student":
            post["coins"] = 0
        else:
            post["students"] = []

        # post user to database
        user_collection.insert_one(post)
        flash("Your account was successfully made! Please login now.")
        return redirect("/user/login")
    else:
        return render_template("register.html")


@user.route("/sign-out", methods=["GET"])
def sign_out():
    """hello."""
    session.pop("email", None)
    flash("You have been logged out successfully.")
    return redirect("/user/login")


@user.route("/classroom", methods=["GET", "PUT", "DELETE"])
def classroom():
    if request.method == "PUT":
        data = request.get_data(as_text=True)
        studentEmail = parse_at_symbol(data)
        putType = parse_type(data)

        if putType == "add":
            user_collection.update({"email": session["email"]},
                                   {"$push": {"students": studentEmail}})
        else:
            putType = int(putType)
            user_collection.update({"email": studentEmail},
                                   {'$set': {'coins': putType}})
        return "PUT request completed."
    elif request.method == "DELETE":
        data = request.get_data(as_text=True)
        studentEmail = parse_at_symbol(data)
        user_collection.update({"email": session["email"]},
                               {"$pull": {"students": studentEmail}})
        return("DELETE request completed.")
    else:
        user = user_collection.find_one({"email": session["email"]})
        students = get_student_db_objects(user["students"])
        assignments = list(assignment_collection.find(
            {"email": session["email"]}))
        return render_template("student.html", len=len(assignments), assignments=assignments, students=students)


# helper functions


def get_student_db_objects(studentEmails):
    studentObjects = []
    for email in studentEmails:
        student = user_collection.find_one({"email": email})
        studentObjects.append(student)
    return studentObjects


def parse_at_symbol(data):
    emailString = ""
    if '&' in data:
        emailString = data[data.index('=') + 1:data.index('&')]
    else:
        emailString = data[data.index('=') + 1:]
    stringPieces = emailString.split("%40")
    return '@'.join(stringPieces)


def parse_type(data):
    data = data.replace('=', 'z', 1)
    putType = data[data.index('=') + 1:]
    return putType
