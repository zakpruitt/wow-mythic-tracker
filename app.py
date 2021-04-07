"""aaa."""
import os
from flask import Flask
from routes.init import init
from routes.user import user
from routes.assignment import assignment

app = Flask(__name__)
app.register_blueprint(init)
app.register_blueprint(user)
app.register_blueprint(assignment)

#app.secret_key = os.environ.get('SECRET')
app.secret_key = "pog"

if __name__ == "__main__":
    app.run(debug=True)


# region
# @app.route("/dungeon/<abbr>", methods=["GET"])
# def dungeon_page(abbr):
#     """HUH."""
#     if 'username' not in session:
#         flash("Please log in or register to view your stats.")
#         return redirect("/")
#     else:
#         dungeon = dungeon_collection.find_one({"shorthand": abbr})

#         if dungeon:
#             return render_template("dungeon.html", dungeon=dungeon,  p_name=dungeon["p_name"])
#         else:
#             return render_template("404.html")
# endregion