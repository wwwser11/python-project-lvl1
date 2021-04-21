#!/usr/bin/env python3

import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?:')
    print('Hello, {}'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name

def even_game():
    name = welcome_user()
    count_of_wins = 0
    game_mover = True
    while game_mover:
        if count_of_wins < 3:
            number = random.randint(0, 100)
            print('Question: ', number)
            user_answer = input('Your answer: ')
            if (number % 2) == 0 and user_answer == 'yes':
                print('Correct!')
                count_of_wins += 1
            elif (number % 2) != 0 and user_answer == 'no':
                print('Correct!')
                count_of_wins += 1
            if (number % 2) == 0 and user_answer != 'yes':
                print(f"'{user_answer}' is wrong answer ;(.\nCorrect answer was 'yes'. Let's try again, {name}!")
            elif (number % 2) != 0 and user_answer != 'no':
                print(f"'{user_answer}' is wrong answer ;(. \n Correct answer was 'no'. Let's try again, {name}!")
        if count_of_wins == 3:
            print(f'Congratulations, {name}!')
            game_mover = False
