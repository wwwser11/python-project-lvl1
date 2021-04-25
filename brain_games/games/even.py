#!/usr/bin/env python3

import random
from brain_games.games.fuctions import welcome_func
from brain_games.games.fuctions.wrong_answer_func import wrong_answer as wrong


def even_game():
    name = welcome_func.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
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
                print(wrong(user_answer, 'yes', name))
            elif (number % 2) != 0 and user_answer != 'no':
                print(wrong(user_answer, 'no', name))
        if count_of_wins == 3:
            print(f'Congratulations, {name}!')
            game_mover = False
