import os
from flask import Flask
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route("/") #/ refers to the default route
def hello():
    return "Hello World...again!"


#'__main__' is the name of the scope in which top-level code executes.
# A module’s __name__ is set equal to '__main__' when read from standard input, a script,
# # or from an interactive prompt.
if __name__=="__main__": 
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True) #change debug=False in actual deployment or project submission 

