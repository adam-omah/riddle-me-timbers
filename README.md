# Riddle Me Timbers!

******

Pirate Themed Riddle me this game, that allows multiple users to play at once attempting to Answer the presented Riddle.
Players will get a point per answer and after a set time the player with the most points will win the round!

The game will be created with Python and Flask Framework.



## User's Journey:

******

Upon a user entering the application they will be asked for their username, once inputted the game will begin.
A user will be presented with either a text or visual riddle and they will have a form field to enter their guesses to the riddle in,
If the guess is the correct answer a point will be added to the user's name in the leaderboard.
If the guess is incorrect the answer will be stored in the area below the riddle itself.
Only the first user to get the answer correct will be awarded the point.
After which another riddle will be presented and the game continues.
The game will either exit after a set period of time or upon pressing a Leave game button.



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

