# Riddle Me Timbers!

******

Pirate Themed Riddle me this game, that allows users to play a quiz attempting to Answer the presented Riddle.
Players will get a point per answer and after ten rounds the player's score will be compared to the current leaderboard.
If the user gets a highscore they will be added to the leader board as a high scorer!

The game will be created with Python and Flask Framework.




## UX
******

This application is styled by a single full width page on desktop, with imagry as background and 
the content centrally aligned. This website is for user's to enjoy a Python Quiz game with a pirate themed setting.
This is achieve by simple prompts to the user to enter their username (Used for tracking & Identification later on).

* Upon which the user is imediately brought to the game page, where they will be asked a series of Pirate based questions.
* The user will be given the choice to answer the question, in which they have 3 attempts to get it correct before failing that round 
* or they may chose to "Skip" the question given for which the round will end & proceed to the next.
* After 10 questions the user will be brought to the leaderboard or end game screen in which if their score was greater than the scores currently there they will be recorded as a high scorer.


## Features
******

### Existing Features
* Username - allows users to choose their name for the entirety of the game.
* score & attempts - user is displayed their score and attempts remaining for their current round.
* Riddles presented - user is given a riddle to solve.
* Answer Input - user guesses the riddle presented, this is then checked against the correct answer for the riddle.
* Round Counter- as the rounds progress, this keeps track of the users progress.
* End game - when user finishes round 10, they are redirected to the end game page.
* Leader board - List of the top ten scorers.


### Features Left to Implement
* Button on Leaderboard/end game page to re-initiate the game for the user.


## Technologies Used
******

* [Python](https://www.python.org/)
        Python Coding Language, Using the [Flask Framework](http://flask.pocoo.org/) to render page templates with the current user data.


## Deployment
******

This project is deployed on [Heroku](https://shiver-me-timbers.herokuapp.com/) it is linked to the Git Repoistory
on [Github](https://github.com/adam-omah/riddle-me-timbers) for which the files are stored as a back up.

## Credits
******

### Content
*  Questions taken from [Pirate questions for kids](http://riddles-for-kids.org/12-pirate-riddles-for-kids/)

### Media
* Media files were found on [Unsplash](https://unsplash.com/)



#### Note's relating to initial planning

******

The application will be built using the TDD method of developement.

Layout mockups: 
* [Mobile](https://wireframe.cc/8MwcuT)
* [Desktop + tablet](https://wireframe.cc/ALckWz)


Initial Idea's for tests:
1. Test for invalid answer
2. Test for valid answer
3. Test for score addition
4. Test for ranking on leaderboard


1. if question is 1+1 and answer of 1 is inputted, fails.
2. if question is 1+1 and answer of 2 is given, test passes.
3. If answer is invalid score remains the same.
4. If answer is valid score is added.
5. If username has highest score, name is listed at top of leaderboard.

Questions relating to the scope of the project:

Leaderboard may be a .txt file?
Riddles to be stored in .json format? or is there a better way to store the data.

