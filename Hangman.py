import random
import time
import sys
from time import localtime, strftime

letterSelection = ['letter', 'LETTER', 'l']
wordSelection = ['word', 'WORD', 'w']
true = ['yes', 'Yes', 'YES']
gameFinished = 0
guessingCount = 0
notInWord = []
hint = []
capital = ''
state = ''
lives = 5
timeStart = time.time()


def dash_word(word):
    for i in word:
        if i == ' ':
            hint.append('  ')
        else:
            hint.append('_ ')
    print_hint()


def print_hint():
    for l in hint:
        print(l, end='')
    print('')


def show_lives():
    print('Lives: %d' % lives)


def is_game_active():
    if lives > 0:
        return True
    else:
        return False


def calculate_time(time_start):
    time_stop = time.time()
    return time_stop - time_start


def print_guessed_letters(letter):
    global gameFinished
    counter = 0
    for i in capital:
        if i == letter:
            hint[counter] = letter + ' '
        counter += 1
    print_hint()
    dashes = 0
    for l in hint:
        if l == '_ ':
            dashes += 1
    if dashes == 0:
        guessing_time = calculate_time(timeStart)
        print("Awesome! You won! It took you", guessingCount, "tries and", round(guessing_time, 2), "s!")
        add_highscore()
        gameFinished = 1
        play_again()


def guessing_letter():
    global guessingCount, lives
    guessingCount += 1
    while True:
        letter = input('Enter the letter: ').upper()
        if letter.isalpha() and len(letter) == 1:
            break
    if letter in capital:
        print_guessed_letters(letter)
        guessing_selection()
    else:
        lives -= 1
        show_lives()
        if is_game_active():
            notInWord.append(letter)
            if notInWord:
                print('Not in word: ', end='')
            for i in notInWord:
                print('%s ' % i, end='')
            print('')
            print_hint()
            guessing_selection()
        else:
            print('Game Over!')
            play_again()


def guessing_word():
    global lives, guessingCount
    guessingCount += 1
    word = input('Enter the word: ').upper()
    if word == capital:
        guessing_time = calculate_time(timeStart)
        print("Awesome! You won! It took you", guessingCount, "tries and", round(guessing_time, 2), "s!")
        add_highscore()
        play_again()
    else:
        lives -= 2
        show_lives()
        if is_game_active():
            print_hint()
            guessing_selection()
        else:
            print('Game Over!')
            play_again()


def guessing_selection():
    while True:
        if gameFinished == 1:
            break
        if lives == 1:
            print('Hint: Capital of ' + state)
        guessing_selection = input('Do you want to guess a \033[92ml\033[0metter or a whole \033[92mw\033[0mord? ')
        if guessing_selection in letterSelection:
            guessing_letter()
            break
        if guessing_selection in wordSelection:
            guessing_word()
            break


def play_again():
    while True:
        answer = input('Type \033[92myes\033[0m to start again or any other key to quit ')
        if answer in true:
            reset_values()
            main()
        else:
            sys.exit()


def reset_values():
    global hint, notInWord,  gameFinished, guessingCount, lives, timeStart
    hint = []
    notInWord = []
    gameFinished = 0
    guessingCount = 0
    lives = 5
    timeStart = time.time()


def random_capital():
    global capital, state
    lines = open('countries_and_capitals.txt').read().splitlines()
    state_capital = random.choice(lines).split(' | ')
    capital = state_capital[1].upper()
    state = state_capital[0]


def add_highscore():
    name = input('Great job! Enter your name to add your score to scoreboard: ')
    showtime = strftime("%d-%m-%Y %H:%M:%S", localtime())
    print(showtime)
    with open('scoreboard.txt', 'w') as f:
        f.write(name + ' | ' + showtime + ' | ' + str(guessingCount) + ' | ' + capital)


def main():
    print('Welcome to the Hangman Game!')
    random_capital()
    dash_word(capital)
    show_lives()
    guessing_selection()


if __name__ == "__main__":
    main()
