import os
from datetime import datetime
from flask import Flask, render_template, make_response, request, redirect, session, g
from wtforms import Form
import random
from random import shuffle
import utills
from utills import write_score, read_scores, sort_scores, print_scores, has_better_score
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)


    
@app.route('/', methods=["GET", "POST"])
def index():
    session.pop('user', None)
    if request.method == ("POST"):
        session['user'] = request.form['username']
        session["score"] = 0
        session["riddle_round"] = 0
        session["attempts_remaining"] = 2
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
        quiz_file = json.load(json_data)
    
    
    if g.user == None:
        return redirect("index.html")
        
    if session["riddle_round"] == 9:
            scores, names = read_scores('data/highscore.txt',' , ')
            sorted_scores = sort_scores(scores, names)
            
            new_name = username
            new_score = session["score"]
            
            if has_better_score(new_score, sorted_scores, 9):
                write_score(new_score, new_name, sorted_scores, 'data/highscore.txt', ' , ')
                
            sorted_scores = sort_scores(scores, names)
            scores, names = read_scores('data/highscore.txt',' , ')
                
            return render_template("end_game.html",
                                    username = username,
                                    current_score = session["score"],
                                    names = names,
                                    highscores = scores,
                                    highscores_users = scores,
                                    highscored_users = names
                                    )
    if request.method == "POST" :
        riddle_guess = request.form["riddle_guess"].lower()
        if  riddle_guess == quiz_file[session["riddle_round"]]["answer"]:
            session["score"] += 1
            session["riddle_round"] += 1
            session.modified = True
        elif riddle_guess == "skip":
            session["riddle_round"] += 1
            session.modified = True
        elif session["riddle_round"] == 10:
            return render_template("end_game.html")
        elif session["attempts_remaining"] == 0:
            session["riddle_round"] += 1
            session["attempts_remaining"] = 2
            session.modified = True
        else:
            session['attempts_remaining'] -= 1
            session.modified = True
            
    return render_template("single_player.html",
                            username = username,
                            question = quiz_file[session["riddle_round"]]["question"], 
                            current_score= session["score"], 
                            riddle_round= session["riddle_round"],
                            attempts_remaining = session["attempts_remaining"] + 1,
                            answer = quiz_file[session["riddle_round"]]["answer"])
        



app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)