#To have access to the environment variables
import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session,
    url_for
#To initalize our new Flaks application
app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []
#Adding an empty list



def add_message(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    #creating a dictionary to store our messages information
    messages.append({"timestamp": now, "from": username, "message": message})




@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    """meaning, so if the username variable is set, then instead of returning our index.html template, we're going to redirect to the contents of the session username variable"""
    if "username" in session: 
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")



@app.route("/chat/<username>", methods=["GET", "POST"])
def user(username):
    """Add and Display chat messages"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))

    return render_template("chat.html", username=username,
                           chat_messages=messages)



# app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
if __name__ == '__main__':
    app.run(debug=True)