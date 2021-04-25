#!/usr/bin/env python3

import random
import prompt
from brain_games.games.fuctions import welcome_func
from brain_games.games.fuctions.wrong_answer_func import wrong_answer as wrong


def prime_number():
    is_prime = ''
    name = welcome_func.welcome_user()
    game_gone = True
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no')
    while game_gone:
        number = random.randint(0, 20)
        print('Question: ', number)
        user_answer = prompt.string('Your answer: ')

        if number == 0 or number == 1:
            is_prime = 'no'
        elif number > 1:
            is_prime = 'yes'
            for i in range(2, number - 1):
                if (number % i) == 0:
                    is_prime = 'no'

        if is_prime == user_answer:
            print('Correct!')
            count += 1
        else:
            print(wrong(user_answer, is_prime, name))
            count = 0

        if count == 3:
            game_gone = False


