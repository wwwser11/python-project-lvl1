import random

GAMECONDITION = 'Find the greatest common divisor of given numbers.'


def question_result():
    set_max_num = 20
    first_num = random.randint(1, set_max_num)
    second_num = random.randint(1, set_max_num)
    print(f'Question: {first_num} {second_num}')
    user_answer = input('Your answer: ')
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num %= second_num
        else:
            second_num %= first_num
    real_num = str(first_num + second_num)
    return user_answer, real_num
