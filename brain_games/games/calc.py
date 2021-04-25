#!/usr/bin/env python3

import random
from brain_games.games.fuctions import welcome_func
from brain_games.games.fuctions.wrong_answer_func import wrong_answer as wrong


def calc_game():
    name = welcome_func.welcome_user()
    print('What is the result of the expression?')
    operator_dict = {1: '+', 2: '-', 3: '*'}
    game_gone = True
    count = 0
    while game_gone:
        random_operator = random.randint(1, 3)
        first_num = random.randint(1, 50)
        second_num = random.randint(1, 50)
        expression = f'{first_num} {operator_dict[random_operator]} {second_num}'
        print('Question: ', expression)
        if random_operator == 3:
            answer = first_num * second_num
        elif random_operator == 2:
            answer = first_num - second_num
        elif random_operator == 1:
            answer = first_num + second_num
        user_answer = input('Your answer: ')
        if user_answer == str(answer):
            print('Correct!')
            count += 1
        else:
            print(wrong(user_answer, answer, name))
            count = 0
        if count == 3:
            game_gone = False
