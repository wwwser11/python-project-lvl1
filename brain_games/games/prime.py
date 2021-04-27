import prompt
import random

GAMECONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no'


def question_result():
    set_max_num = 20
    is_prime = ''
    number = random.randint(0, set_max_num)
    print('Question: {}'.format(str(number)))
    user_answer = prompt.string('Your answer: ')
    if number == 0:
        is_prime = 'no'
    elif number == 1:
        is_prime = 'no'
    elif number > 1:
        is_prime = 'yes'
        for i in range(2, number - 1):
            if (number % i) == 0:
                is_prime = 'no'
    return user_answer, is_prime
