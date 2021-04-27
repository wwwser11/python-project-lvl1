import random

GAMECONDITION = 'What is the result of the expression?'


def question_result():
    operator_dict = {1: '+', 2: '-', 3: '*'}
    answer = ''
    set_max_num = 50
    random_operator = random.randint(1, 3)
    first_num = random.randint(1, set_max_num)
    second_num = random.randint(1, set_max_num)
    expression = (
        f'{first_num} {operator_dict[random_operator]} {second_num}'
    )
    print('Question: {}'.format(str(expression)))
    if random_operator == 3:
        answer = first_num * second_num
    elif random_operator == 2:
        answer = first_num - second_num
    elif random_operator == 1:
        answer = first_num + second_num
    user_answer = input('Your answer: ')
    return user_answer, str(answer)
