#!/usr/bin/env python3

import prompt
from brain_games.games.fuctions import welcome_func
from brain_games.games.fuctions.progression import progression
from brain_games.games.fuctions.wrong_answer_func import wrong_answer as wrong


def brain_progression():
    name = welcome_func.welcome_user()
    game_gone = True
    count = 0
    print('What number is missing in the progression?')
    while game_gone:
        hide_and_list = progression()
        list_of_progression = hide_and_list[1]
        hide_num = hide_and_list[0]
        print('Question: ', ' '.join(list_of_progression))
        user_answer = prompt.string('Your answer: ')
        if user_answer == hide_num:
            print('Correct!')
            count += 1
        else:
            print(wrong(user_answer, hide_num, name))
            count = 0
        if count == 3:
            game_gone = False
