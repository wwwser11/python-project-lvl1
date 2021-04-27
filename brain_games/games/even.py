import random

GAMECONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_result():
    answer = ''
    set_max_num = 20
    number = random.randint(0, set_max_num)
    print('Question: {}'.format(str(number)))
    user_answer = input('Your answer: ')
    if (number % 2) == 0:
        answer = 'yes'
    elif (number % 2) != 0:
        answer = 'no'
    return user_answer, answer
