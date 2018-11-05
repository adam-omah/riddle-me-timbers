import os
from datetime import datetime
from flask import Flask, render_template, make_response, request, redirect, session, g
from wtforms import Form
import random
from random import shuffle
import utills
from utills import write_to_file, add_one_score, add_one, remove_attempt, reset_attempts,skip_question, session_cookie, set_score, set_attempts, set_round
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)

# this will later be the riddle data file. (probably json.)

question_asked = [0,1,2,3,4,5,6,7,8,9,10,11,12]


riddle_round = 0
score = 0
attempts_remaining = 2
    
@app.route('/', methods=["GET", "POST"])
def index():
    session.pop('user', None)
    if request.method == ("POST"):
        session['user'] = request.form['username']
        return redirect(request.form["username"])
    return render_template("index.html")


# Set g.user to none before request, set g.user to user if user is in session
@app.before_request
def check_if_session():
    g.user = None
    if 'user' in session :
        g.user = session['user']
        
        

@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    # check to see if a user is in session before going to the game page
    
    with open('data/questions.json') as json_data:
        parsed_json = json.load(json_data)
            
    
    if g.user:
        set_attempts()
        set_round()
        set_score()
        return render_template("single_player.html",
                            username = username,
                            question = parsed_json[riddle_round]["question"], 
                            current_score= [score], 
                            riddle_round= [riddle_round],
                            attempts_remaining = [attempts_remaining],
                            answer = parsed_json[riddle_round]["answer"])
    else:
        return redirect("index.html")
    
    
    if request.method == ("POST"):
        riddle_guess = request.form["riddle_guess"].lower()
 
        if  riddle_guess == parsed_json[session['riddle_round']]['answer']:
            session['score'] +=1
            session['riddle_round'] += 1
            session.modified = True
        elif riddle_guess == "skip":
            session['riddle_round'] += 1
            session.modified = True
        else:
            session['attempts_remaining'] -= 1
            session.modified = True
    
    if session['riddle_round'] == 9:
        return render_template("end_game.html")
    
    if session['attempts_remaining'] == 0:
        session['riddle_round'] += 1
        session['attempts_remaining'] = 2
        session.modified = True
    
        



app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)