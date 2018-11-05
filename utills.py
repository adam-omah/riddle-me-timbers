from flask import make_response

def write_to_file(filename,data):
    """ handle the process of writing data to a file """
    with open(filename, "a") as file:
        file.writelines(data)

def end_game():
    return render_template("end_game.html")

def add_one(variable):
    session['variable'] = session['variable'] + 1
    session.modified = True
    
def session_cookie(name,key,value):
    resp = make_response('name')
    resp.set_cookie('key','value')

def set_score():
    user_score = make_response('User score')
    user_score.set_cookie('user_score','0')
    return user_score

def set_round():
    user_round = make_response('User round')
    user_round.set_cookie('round','0')
    return user_round

def set_attempts():
    user_attempts = make_response('User Attempts')
    user_attempts.set_cookie('user_attempts_remaining','2')
    return user_attempts

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

def shuffle_questions():
    global question_asked
    shuffle(question_asked)