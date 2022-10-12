"""A madlib game that compliments its users."""

from random import sample

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
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)
    #print(compliments) - prints when refresh brwoser

    return render_template("compliment.html", person=player,
     compliments=compliments)
     #name of variblae, like key, call whatver i want; the left is same as line 49 


@app.route("/game")
def show_madlib_form():
    """User's response to "Would you like to play a game?"""

    yes_game = request.args.get("yes")
    no_game = request.args.get("no")
    
    if yes_game:
        #nice_things = sample(COMPLIMENTS, 3)
        return render_template("game.html", yes=yes_game)
    else:
        return render_template("goodbye.html", no=no_game)


@app.route("/madlib", methods=['POST'])
def show_madlib():
    """User's response to playing game """

    person = request.form.get("person")
    color = request.form.get("color")
    adjective = request.form.get("adjective")
    place = request.form.get("place")
    adverb = request.form.get("adverb")
    verb = request.form.get("verb")
    day = request.form.get("day")
    transport = request.form.get("transport")
    
    

    return render_template("madlib.html", 
    person=person, color=color, transport=transport, adjective=adjective, day=day, adverb=adverb, verb = verb, place = place)
    


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
