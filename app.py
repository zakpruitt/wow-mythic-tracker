from flask import Flask, redirect, url_for, render_template, request, session, g, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET')

cluster = pymongo.MongoClient(os.environ.get('MONGODB_URI'))
db = cluster["wow-data"]
user_collection = db["user-data"]
dungeon_collection = db["dungeon-data"]


@app.before_request
def before_request():
    if 'username' in session:
        user = user_collection.find_one({"username": session["username"]})
        g.user = user
    else:
        pass


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop("username", None)
        username = request.form["username"]
        password = request.form["password"]

        user = user_collection.find_one({"username": username})
        if user and check_password_hash(user["password"], password):
            session["username"] = user["username"]
            return redirect("/")
        else:
            flash("Incorrect username or password.")
            return redirect("/login")
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        user = user_collection.find_one({"username": username})
        if user:
            flash("Unfortunately, that username is already taken. Please try another.")
            return redirect("/register")

        password = request.form["password"]
        cpassword = request.form["cpassword"]
        if password != cpassword:
            flash("Your passwords did not match.")
            return redirect("/register")

        spec = request.form["spec"]
        hashed_password = generate_password_hash(password, method="sha256")

        post = {
            "username": username,
            "password": hashed_password,
            "spec": spec,
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
            "plaguefall": {
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
            "tirna_scithe": {
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
            "atonement": {
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
            "theatre": {
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
            "de_other_side": {
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
            "spires": {
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
            "sanguine_depths": {
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
            }
        }
        user_collection.insert_one(post)
        flash("Your account was successfully made! Please login now.")
        return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/sign-out", methods=["GET"])
def sign_out():
    session.pop("username", None)
    return redirect("/")
    

@app.route("/dungeon/<abbr>", methods=["GET"])
def dungeon_page(abbr):
    if 'username' not in session:
        flash("Please log in or register to view your stats.")
        return redirect("/")
    else:
        dungeon = dungeon_collection.find_one({"shorthand": abbr})

        if dungeon:
            return render_template("dungeon.html", dungeon=dungeon,  p_name=dungeon["p_name"])
        else:
            return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)
