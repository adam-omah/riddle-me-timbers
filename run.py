import os
from datetime import datetime
from flask import Flask, render_template, request, redirect
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import random

app = Flask(__name__)


# this will later be the riddle data file. (probably json.)
riddle_list =[1,2,3,4]
round_count = [10]


def write_to_file(filename,data):
    """ handle the process of writing data to a file """
    with open(filename, "a") as file:
        file.writelines(data)
        
def get_all_wrong_answers():
    """ get all of the messages and seperate them with a `br` """
    messages = []
    with open("data/messages.txt", "r") as chat_messages:
        messages = chat_messages.readlines()
    return messages
    
def add_wrong_answer(username, message):
    """ Add messages to message text file"""
    # write the chat messages to messages.txt file 
    write_to_file("data/messages.txt", "({0}) : {1}\n".format(
            username.title(),
            message))


def next_round():
    if round_count < 11:
        riddle_list += 1

def end_game():
    return render_template("end_game.html")

    
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == ("POST"):
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")

@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    
    
    if request.method == ("POST"):
        
        # Set round count to 0 for begining of game, picks k* ammount of questions to use for the game.
        riddle_round = 0
        if riddle_round == 0:
            riddles_this_game = random.sample(riddle_list, k=4)
        
        if riddle_round == 3:
            end_game()
        
        riddle_guess = request.form["riddle_guess"].lower()
        score = 0
        attempts_remaining = 3
        
        
        if riddles_this_game[riddle_round]["answer"] == riddle_guess:
            score += 1
            riddle_round += 1
        elif attempts_remaining == 0:
            riddle_round += 1
        else:
            attempts_remaining -= 1
            add_wrong_answer(username.title, riddle_guess)
        
        #display wrong answers 
        wronganswers = get_all_wrong_answers()
        
        
        # Render single player mode for username + identifiers for html page elements.
        return render_template("single_player.html",
                            username=username, 
                            wrong_answers=wronganswers, 
                            riddles=riddles_this_game, 
                            current_score=score, 
                            riddle_round=riddle_round,
                            attempts_remaining=attempts_remaining)
        



app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)