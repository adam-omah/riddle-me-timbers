import os
from datetime import datetime
from flask import Flask, render_template, request, redirect
from wtforms import Form
import random

app = Flask(__name__)


# this will later be the riddle data file. (probably json.)
round_count = [10]
questions = ["What is 1+1","What is 2+2","What is 3+3","What is 3+3"]
answers = ["2","4","6","8"]

question_dict = {"What is 1+1":"2","What is 2+2":"4", "What is 3+3":"6", "What is 4+4?":"8"}

score = 0
riddle_round = 0
attempts_remaining = 2


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

    
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == ("POST"):
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")

@app.route('/<username>', methods=["GET", "POST"])
def user(username):

    question = questions[riddle_round]
    
    if attempts_remaining == 0:
        add_one_round()
        reset_attempts()
    
    if request.method == ("POST"):
        riddle_guess = request.form["riddle_guess"].lower()
 
        if  riddle_guess == answers[riddle_round]:
            add_one_score()
            add_one_round()
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