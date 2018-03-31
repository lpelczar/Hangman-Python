# Hangman in Python

## Story

Evil SKYNET is trying to take control over the world. And guess who is the only hope for the mankind? 
Yes, you're right - it's you! And you must prove your skills, knowledge and intelligence by showing that 
you are smart and able to guess words!

Create a script that has a list of European capitals, pick one of them randomly and let the user guess it. 
At the beginning program should represent each letter as a dash ("_") and display them at the screen. Additionally, 
program should show player's life points (let's say, 5).

Program should ask the user if he/she would like to guess a letter or whole word(s). Next, program waits for the user 
to enter letter or word. If entered letter doesn't exist in word or entered word is not correct - player will loose 
a life point. If this action brings player life to zero - the game is over!
If the player survives wrong letter guess - that letter should be added to "not-in-word" list and be displayed at the screen.
If the player guesses final letter or whole word(s) - he/she is the winner! And our world is safe ! :) 

## Requirements

- Please start with a flowchart! You can draw first versions of flowchart on paper to discuss it and modify 
if it's faster for you than drawing with mouse.
- Capital names should be in English and capital letters (i.e. LONDON, PARIS, WARSAW).
- Program shouldn't be case sensitive - i.e. no matter if the user enters d or D, it should count as D.
- Creating your own functions and using them well will make your code clearer and allow you to get 10 points for 
clean code if there will be no problems with it's readability.
- Add a question about starting program once again after user win/loose. 
- Add an information about guessing count and guessing time at the end of game (i.e. "You guessed after 12 letters. 
It took you 45 seconds").
- There is a file containing list of countries and their capitals (i.e. Poland | Warsaw). 
Your program should read that file at the beginning and randomly select one country-capital pair.
Then, the capital should be the target word(s) to guess. The country should be also remembered -
if player will remain on his/her last life points program should display a hint (i.e. "The capital of Poland").
- Guessing whole word should be more-risk-more-reward. So, successful guess can save some time, but failing 
whole word guess should result in loosing 2 life points!
- Add high score - everyone like to be proud of his/her successes. At the end of successful game program
should ask user for his/her name and save that information to a file - name| date | guessing_time | guessing_tries 
| guessed_word (i.e. Marcin | 26.10.2016 14:15 | 45 | Warsaw).
- Expand high score - program should remember 10 best scores (read from and write to a file) and display them at 
the end, after success / failure.
- Add ASCII art! How awesome it will be if after each wrong guess a part of hangman will appear? Or a spaceship
will be closer to the Earth? Or something different - use your imagination! :)

## More info

Project made for [Codecool](https://codecool.com/) programming course.
