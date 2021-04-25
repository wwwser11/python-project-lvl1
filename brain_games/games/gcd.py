#!/usr/bin/env python3

import random
from brain_games.games.fuctions import welcome_func
from brain_games.games.fuctions.gcd_func import gcd
from brain_games.games.fuctions.wrong_answer_func import wrong_answer as wrong


def greatest_common_divisor_game():
    name = welcome_func.welcome_user()
    game_gone = True
    count = 0
    print('Find the greatest common divisor of given numbers.')
    while game_gone:
        first_num = random.randint(1, 50)
        second_num = random.randint(1, 50)
        print(f'Question: {first_num} {second_num}')
        real_num = gcd(first_num, second_num)
        user_answer = input('Your answer: ')
        if user_answer != str(real_num):
            print(wrong(user_answer, real_num, name))
            count = 0
        else:
            print('Correct!')
            count += 1
        if count == 3:
            game_gone = False
