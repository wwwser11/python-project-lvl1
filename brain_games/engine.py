from brain_games.welcome_func import welcome_user


def engine(game):
    name = welcome_user()
    print(game.GAMECONDITION)
    for i in range(3):
        qr = game.question_result()
        if qr[0] == qr[1]:
            print('Correct')
        else:
            print(f"'{qr[0]}' is wrong answer ;(.\nCorrect answer was '{qr[1]}'.)"
                  f" Let's try again, {name}!")
            break
    else:
        print('Congratulations, {}!'.format(name))
