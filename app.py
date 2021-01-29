import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/") #/ refers to the default route
@app.route("/get_tasks")
def get_tasks():
    tasks = mongo.db.tasks.find()
    return render_template("tasks.html", tasks=tasks) #the second tasks refer to mongo.db.tasks.find()


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

#'__main__' is the name of the scope in which top-level code executes.
# A module’s __name__ is set equal to '__main__' when read from standard input, a script,
# # or from an interactive prompt.
if __name__=="__main__": 
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True) #change debug=False in actual deployment or project submission 

