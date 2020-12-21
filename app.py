from flask import Flask, redirect, url_for, render_template
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

cluster = pymongo.MongoClient("mongodb+srv://zak:1234@zak-cluster.gp6ka.mongodb.net/wow-data?retryWrites=true&w=majority")
db = cluster["wow-data"]
collection = db["user-data"]

post = { "username": "zak", 
         "password": "1234",
         "spec": "windwalker",
         "necrotic-wake": {
            "+0": 0,
            "+1": 0,
            "+2": 0,
            "+3": 0,
            "+4": 0,
            "+5": 0,
            "+6": 0,
            "+7": 0,
            "+8": 0,
            "+9": 0,
            "+10 and above": 0
         },
         "plaguefall": {
            "+0": 0,
            "+1": 0,
            "+2": 0,
            "+3": 0,
            "+4": 0,
            "+5": 0,
            "+6": 0,
            "+7": 0,
            "+8": 0,
            "+9": 0,
            "+10 and above": 0
         },
         "tirna-scithe": {
            "+0": 0,
            "+1": 0,
            "+2": 0,
            "+3": 0,
            "+4": 0,
            "+5": 0,
            "+6": 0,
            "+7": 0,
            "+8": 0,
            "+9": 0,
            "+10 and above": 0
         },
         "atonement": {
            "+0": 0,
            "+1": 0,
            "+2": 0,
            "+3": 0,
            "+4": 0,
            "+5": 0,
            "+6": 0,
            "+7": 0,
            "+8": 0,
            "+9": 0,
            "+10 and above": 0
         },
         "theatre": {
            "+0": 0,
            "+1": 0,
            "+2": 0,
            "+3": 0,
            "+4": 0,
            "+5": 0,
            "+6": 0,
            "+7": 0,
            "+8": 0,
            "+9": 0,
            "+10 and above": 0
         },
         "de-other-side": {
            "+0": 0,
            "+1": 0,
            "+2": 0,
            "+3": 0,
            "+4": 0,
            "+5": 0,
            "+6": 0,
            "+7": 0,
            "+8": 0,
            "+9": 0,
            "+10 and above": 0
         },
         "spires": {
            "+0": 0,
            "+1": 0,
            "+2": 0,
            "+3": 0,
            "+4": 0,
            "+5": 0,
            "+6": 0,
            "+7": 0,
            "+8": 0,
            "+9": 0,
            "+10 and above": 0
         },
         "sanguine-depths": {
            "+0": 0,
            "+1": 0,
            "+2": 0,
            "+3": 0,
            "+4": 0,
            "+5": 0,
            "+6": 0,
            "+7": 0,
            "+8": 0,
            "+9": 0,
            "+10 and above": 0
         }
       }

collection.insert_one(post)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
