from flask import Flask, render_template, g, request, session, Blueprint
from pymongo import MongoClient
from .init import assignment_collection

assignment = Blueprint('assignment', __name__, url_prefix='/assignment')


@assignment.route("/create", methods=["GET", "POST"])
def create():
    """HUH."""
    if request.method == "GET": 
        return render_template("create.html")
    elif request.method == "POST":
        last_key = list(request.form.keys())[len(request.form) - 1]
        print(last_key[last_key.rindex('-')+1:])

        print(g.user["email"])
        return render_template("create.html")


    