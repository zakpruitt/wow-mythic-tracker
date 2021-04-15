"""aaa."""
import os
from flask import Flask
from routes.init import init
from routes.user import user
from routes.assignment import assignment
from routes.report import report

app = Flask(__name__)
app.register_blueprint(init)
app.register_blueprint(user)
app.register_blueprint(assignment)
app.register_blueprint(report)


#app.secret_key = os.environ.get('SECRET')
app.secret_key = "pog"

if __name__ == "__main__":
    app.run(debug=True)