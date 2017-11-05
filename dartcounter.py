from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app = Flask(__name__)
Bootstrap(app)
app.debug = True
app.secret_key = "123456"

toolbar = DebugToolbarExtension(app)

class Game:
    def __init__(self):
        self.players = [1, 2, 3, 4]
        self.mode = ["Single Out", "Double Out"]
        self.points = [301, 401, 501, 601, 701, 801]



dings = Game()



# Menu Route
@app.route("/", methods=["GET", "POST"])
def menu():
    if request.method == "GET":
            players = dings.players
            mode = dings.mode
            points = dings.points
            return render_template("index.html", players=players, mode=mode, points=points)

# Game Route
@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        players = request.args["players"]
        mode = request.args["mode"]
        points = request.args["points"]
        print("Empfangen: " + players + " - " + mode + " - " + points)
        return render_template("game.html", players=players, mode=mode, points=points)

# Statistics Route
@app.route("/statistics")
def statistics():
    return render_template("statistics.html")


if __name__ == "__main__":
    app.run(debug=True)
