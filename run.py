import os
from datetime import datetime
from flask import Flask, render_template, request, redirect
from wtforms import Form
import random

app = Flask(__name__)


# this will later be the riddle data file. (probably json.)

questions = [
    "If you are a pirate And you get in a fight You might need to wear this If you lose half your sight",
"This item contains shiny things You’ll have to wait to find out what It’s what you’ll end up digging up Once you’ve found the X that marks the spot",
"It sits on a pirate’s shoulder And doesn’t ever fly away The funniest thing about it Is that it repeats what you say",
"The image on this pirate flag Is sure to give people a fright It has parts of a skeleton On a background as dark as night",
"A ship drops this to stay still Even if the water’s calm It is also a tattoo You can see on Popeye’s arm",
"A pirate who’s lost a tibia Might replace it with this thing That will help him to still walk around Instead of just hopping",
"This was a famous pirate One who was truly feared A color and some facial hair This pirate was _ _ _ _ _ _ _ _ _ _",
"When looking for buried gold This item helps a lot As on this piece of paper Is where X marks the spot",
"If you’re sailing on a pirate ship To find your way you’ll need at least This item that will help guide the way By pointing north, south, west and east",
"This pirate phrase is what you get If you take a two by four And then place it on a shelf Inside of a freezer door",
"If you follow a treasure map At the end of a successful quest You might hope to find this inside Of the buried treasure chest",
"If you want to be a pirate You will need this without fail So that you can travel around You need something you can sail"
]
answers = ["eye patch","treasure chest","parrot","jolly roger","anchor","wooden leg","blackbeard","treasure map","compass","shiver me timbers","gold coins","ship"]

question_asked = [0,1,2,3,4,5,6,7,8,9,10,11,12]


score = 0
riddle_round = 0
attempts_remaining = 2

player_one_score = 0
player_two_score = 0
player_three_score = 0
player_four_score = 0



def write_to_file(filename,data):
    """ handle the process of writing data to a file """
    with open(filename, "a") as file:
        file.writelines(data)

def end_game():
    return render_template("end_game.html")
    
def add_one_round():
    global riddle_round
    riddle_round += 1
    
def add_one_score():
    global score
    score += 1
    
def remove_attempt():
    global attempts_remaining
    attempts_remaining -= 1

def reset_attempts():
    global attempts_remaining
    attempts_remaining = 2

def skip_question():
    global riddle_round
    riddle_round += 1
    global attempts_remaining
    attempts_remaining = 2
    

    
    
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == ("POST"):
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")

@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    
    if attempts_remaining == 0:
        add_one_round()
        reset_attempts()
    
    if request.method == ("POST"):
        riddle_guess = request.form["riddle_guess"].lower()
 
        if  riddle_guess == answers[riddle_round]:
            add_one_score()
            add_one_round()
        elif riddle_guess == "skip":
            skip_question()
        else:
            remove_attempt()
        
        
        
     # Render single player mode for username + identifiers for html page elements.
    return render_template("single_player.html",
                            username=username,
                            question = questions[riddle_round], 
                            current_score=score, 
                            riddle_round=riddle_round,
                            attempts_remaining=attempts_remaining + 1,
                            answer=answers[riddle_round])
        



app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)