import random
import time
import sys
import os
from time import localtime, strftime

letterSelection = ['letter', 'LETTER', 'l']
wordSelection = ['word', 'WORD', 'w']
true = ['yes', 'Yes', 'YES']
gameFinished = 0
guessingCount = 0
guessing_time = 0
notInWord = []
hint = []
timeN = []
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


def print_spaced(word):
    for i in word:
        print('%s '% i, end='')
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
    global gameFinished, guessing_time
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
        clear_terminal()
        print_spaced(capital)
        show_lives()
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
        clear_terminal()
        print_guessed_letters(letter)
        show_lives()
        print_not_in_word()
        guessing_selection()
    elif letter in notInWord:
        print('You have already typed that letter!')
        guessing_selection()
    else:
        lives -= 1
        clear_terminal()
        print_hint()
        show_lives()
        if is_game_active():
            notInWord.append(letter)
            print_not_in_word()
            guessing_selection()
        else:
            print('Game Over!')
            play_again()


def print_not_in_word():
    if notInWord:
        print('Not in word: ', end='')
    for i in notInWord:
        print('%s ' % i, end='')
    print('')


def guessing_word():
    global lives, guessingCount, guessing_time
    guessingCount += 1
    word = input('Enter the word: ').upper()
    if word == capital:
        guessing_time = calculate_time(timeStart)
        clear_terminal()
        print_spaced(capital)
        show_lives()
        print("Awesome! You won! It took you", guessingCount, "tries and", round(guessing_time, 2), "s!")
        add_highscore()
        play_again()
    else:
        lives -= 2
        if lives < 0:
            lives = 0
        if is_game_active():
            clear_terminal()
            print_hint()
            show_lives()
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


def show_highscore():
    with open('scoreboard.txt', 'r') as f:
        i = 1
        for line in f:
            if i >= 1 and i <= 10:
                print(line)
            i += 1


def read_highscore():
    global timeN
    with open('scoreboard.txt', 'r') as f:
        for line in f:
            timeN.append(find_between(line, '> ', ' <'))


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def add_highscore():
    read_highscore()
    name = input('Great job! Enter your name to add your score to scoreboard: ')
    showtime = strftime("%d-%m-%Y %H:%M:%S", localtime())
    round_time = str(round(guessing_time, 2))

    f = open('scoreboard.txt', 'r')
    contents = f.readlines()
    f.close()
    value = name + ' | ' + showtime + ' | ' + str(guessingCount) + ' |> ' + round_time + ' <| ' + capital+'\n'

    if not timeN:
        contents.insert(0, value)
        f = open('scoreboard.txt', 'w')
        contents = "".join(contents)
        f.write(contents)
        f.close()

    if float(round_time) > float(timeN[-1]):
        contents.insert(timeN.index(timeN[-1])+1, value)
        f = open('scoreboard.txt', 'w')
        contents = "".join(contents)
        f.write(contents)
        f.close()
    else:
        for i in timeN:
            if float(i) > float(round_time):
                contents.insert(timeN.index(i), value)
                f = open('scoreboard.txt', 'w')
                contents = "".join(contents)
                f.write(contents)
                f.close()
                break
            else:
                continue


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Welcome to Hangman game! Have fun!')
    print_hangman(lives)


def print_ascii(start_line, end_line):
    with open('ascii_hangman.txt', 'r') as f:
        i = 1
        for line in f:
            if i >= start_line and i <= end_line:
                print (line)
            i += 1


def print_hangman(live):
    if live == 0:
        print_ascii(2,11)
    elif live == 1:
        print_ascii(14,23)
    elif live == 2:
        print_ascii(26,35)
    elif live == 3:
        print_ascii(37,46)
    elif live == 4:
        print_ascii(48,57)
    elif live == 5:
        print_ascii(59,68)


def main():
    clear_terminal()
    show_highscore()
    random_capital()
    dash_word(capital)
    show_lives()
    guessing_selection()


if __name__ == "__main__":
    main()
