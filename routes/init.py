"""assas."""
from flask import Flask, render_template, g, request, session, Blueprint, redirect
from pymongo import MongoClient
import os

init = Blueprint('init', __name__)

cluster = MongoClient('mongodb+srv://zak:1234@zak-cluster.gp6ka.mongodb.net/coin-data?retryWrites=true&w=majority')
#cluster = MongoClient(os.environ.get('MONGODB_URI'))
db = cluster["coin-data"]
user_collection = db["user"]
assignment_collection = db["assignment"]


@init.before_app_request
def find_user():
    """HUH."""
    if request.endpoint not in ["user.login", "user.register"]:
        if 'email' in session:
            user = user_collection.find_one({"email": session["email"]})
            g.user = user
        else:
            return redirect("/user/login")


@init.route("/", methods=["GET"])
def home():
    """HUH."""
    assignments = list(assignment_collection.find({"email": session["email"]}))
    return render_template("index.html", len = len(assignments), assignments = assignments)

