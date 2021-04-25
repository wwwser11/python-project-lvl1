#!/usr/bin/env python3

import random


def progression():
    list_of_progression = []
    hide_and_list = []
    start_point = random.randint(0, 50)
    step_size = random.randint(1, 20)
    list_size = random.randint(4, 9)
    position_of_hide_num = random.randint(0, list_size)
    list_of_progression.append(str(start_point))
    for i in range(list_size):
        list_of_progression.append(str(int(list_of_progression[i]) + step_size))
    hide_num = list_of_progression[position_of_hide_num]
    hide_and_list.append(hide_num)
    list_of_progression[position_of_hide_num] = '..'
    hide_and_list.append(list_of_progression)
    return hide_and_list
