from flask import make_response, session
import json

        
def write_score(score, name, scores, filename, separator=','):
    """writes a score with a name to a file, in a specified format"""
    scores.append((score, name))
    with open(filename,'w') as f:
        for s in scores:
            f.write(separator.join(map(str, s)) + '\n')

def read_scores(filename, separator=','):
    """reads scores and names from a file, and returns a list of each"""
    scores = []
    names = []

    with open(filename) as f:
        for score in f:
            score, name = score.strip().split(separator)
            scores.append(int(score))
            names.append(name)
    return scores, names

def sort_scores(scores, names, reverse_bool=True):
    """sorts the scores from greatest to least and returns in a list of tuples format"""
    return sorted(zip(scores,names), reverse=reverse_bool)

def print_scores(score_list, separator=' ', top_amount=10):
    """prints the number of leaderboard scores stated"""
    for score_tuple in score_list[:top_amount]:
        print(separator.join(map(str, score_tuple)))

def has_better_score(score, scores, leaderboard_len=10):
    """returns if the score should be written to a file"""
    if (len(scores) > leaderboard_len and score >= scores[leaderboard_len - 1][0]) or len(scores) <= leaderboard_len:
        return True
    return False