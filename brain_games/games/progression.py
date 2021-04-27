import prompt
import random

GAMECONDITION = 'What number is missing in the progression?'


def question_result():
    list_of_progression = []
    max_start_point = 50
    max_step_size = 20
    start_point = random.randint(0, max_start_point)
    step_size = random.randint(1, max_step_size)
    list_size = random.randint(4, 9)
    position_of_hide_num = random.randint(0, list_size)
    list_of_progression.append(str(start_point))
    for num in range(list_size):
        list_of_progression.append(str
                                   (int(list_of_progression[num]) + step_size))
    hide_num = list_of_progression[position_of_hide_num]
    list_of_progression[position_of_hide_num] = '..'
    print('Question: ', ' '.join(list_of_progression))
    user_answer = prompt.string('Your answer: ')
    return user_answer, hide_num
