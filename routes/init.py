"""assas."""
from flask import Flask, render_template, g, request, session, Blueprint
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
    if 'email' in session:
        user = user_collection.find_one({"email": session["email"]})
        g.user = user
    else:
        pass


@init.route("/", methods=["GET"])
def home():
    """HUH."""
    return render_template("index.html")

