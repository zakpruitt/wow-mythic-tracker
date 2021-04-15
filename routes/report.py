from flask import Flask, render_template, g, request, session, Blueprint, flash, redirect
from pymongo import MongoClient
from .init import assignment_collection


report = Blueprint('report', __name__, url_prefix='/report')


@report.route("/<assignmentId>", methods=["GET"])
def load_report(assignmentId):
    print(assignmentId)
    assignment = assignment_collection.find_one(
        {"_id": assignmentId, "email": g.user["email"]})
    if not assignment:
        flash("Not found.")
        return redirect("/assignment/create")
        #return render_template("dungeon.html", dungeon=dungeon,  p_name=dungeon["p_name"])
    return render_template("report.html", id=assignmentId)

