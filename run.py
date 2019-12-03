#To have access to the environment variables
import os 
from flask import Flask
#To initalize our new Flaks application
app = Flask(__name__)




@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a message use: /USERNAME/MESSAGE"


@app.route("/<username>")
def user(username):
    return "Hi " + username


@app.route("/<username>/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username, message)
    #{} means returning a string


# app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
if __name__ == '__main__':
    app.run(debug=True)