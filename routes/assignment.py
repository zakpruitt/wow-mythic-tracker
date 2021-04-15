from flask import Flask, render_template, g, request, session, Blueprint, flash, redirect
from pymongo import MongoClient
from uuid import uuid4
from .init import assignment_collection
import re, string, random

assignment = Blueprint('assignment', __name__, url_prefix='/assignment')


@assignment.route("/create", methods=["GET", "POST"])
def create():
    """HUH."""
    if request.method == "GET":
        return render_template("create.html")
    elif request.method == "POST":
        data = request.form.to_dict()
        length = get_length(list(data.keys()))

        # check if title is in use
        assignment = assignment_collection.find_one({
            "email": g.user["email"],
            "title": data["assignment-title"]
        })
        if assignment:
            flash("You already have an assignment created with that title.")
            return redirect("/assignment/create")

        # create post
        post = {
            "_id": str(uuid4()),
            "email": g.user["email"],
            "title": data["assignment-title"],
            "urlKey": generate_url()
        }

        for i in range(1, length + 1):
            # INITIALIZE DICT
            temp = {}

            # TITLE
            temp[f"question{i}Title"] = data[f"title{i}"]

            # QUESTION CHOICES
            question_amount = get_question_choice_amount(i, data.keys())
            for j in range(1, question_amount + 1):
                temp[f"question{i}Choice{j}"] = data[f"q{i}option{j}"]

            # CORRECT CHOICE NUMBER
            correctKey = get_question_correct_key(i, data.keys())
            temp[f"correctNumber"] = parse_correct_key_number(correctKey)

            # ADD TO POST
            post[f"question{i}"] = temp

        # insert into db
        assignment_collection.insert_one(post)
        return render_template("create.html")


@assignment.route("/<key>", methods=["GET"])
def key_detector(key):
    """ Detects key in database and redirects user to corresponding original field.
    Args:
        key (string): The URL's unique key
    Returns:
        function: Redirects to original page or 404 page.
    """

    # url = table.find_one({"key": key})

    # if url:
    #     return redirect(url["original"])
    # else:
    #     return "404"
    pass


# region URL FUNCTIONS


def generate_url():
    key = get_random_string()
    url = assignment_collection.find_one({"urlKey": key})

    # makes sure url is unique
    while url:
        key = get_random_string()
        url = assignment_collection.find_one({"urlKey": key})

    return key


def get_random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(6))


# endregion

# region HELPER FUNCTIONS


def get_length(formKeys):
    last_key = formKeys[len(formKeys) - 1]
    length = re.search(r"[0-9]+", last_key).group()
    return int(length)


def get_question_choice_amount(questionNumber, keys):
    if f"q{questionNumber}option3" in keys:
        return 4
    else:
        return 2


def get_question_correct_key(questionNumber, keys):
    try:
        for i in range(1, 5):
            if f"q{questionNumber}correct{i}" in keys:
                return f"q{questionNumber}correct{i}"
        raise Exception("No correct answer found.")
    except Exception:
        print("No correct answer found.")


def parse_correct_key_number(correctKey):
    return int(re.search(r"(\d+)$", correctKey).group())


# endregion
