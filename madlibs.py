"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user. Ask if they'd like to play a game."""

    return render_template("hello.html")

@app.route("/game")
def show_madlib_form():
    """Confirm if player wants to play and send them to Madlibs."""
    play_confirm = request.args.get('confirm')

    if play_confirm:
        return render_template("game.html")
    else:  
        return render_template("goodbye.html")

@app.route("/madlib")
def show_madlib():
    """Display the completed Madlib"""

    person_in = request.args.get('person')
    color_in = request.args.get('color')
    noun_in = request.args.get('noun')
    adj_in = request.args.get('adj')

    return render_template("madlib.html",
                            person = person_in,
                            color = color_in,
                            noun = noun_in,
                            adjective = adj_in)

@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
