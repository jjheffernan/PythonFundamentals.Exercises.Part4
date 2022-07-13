# test comment
"""
higher or lower guessing game
copied from Previous Exercise (.Exercises.Part3)
created by jj on 8 jul 2022
"""

import random

player_num = 0
comp_guess = 0
game_status = True

print("""
    Welcome to JJ's lovely guessing game. Input a guess from 0-10 \n
    """)


def computer_guess():
    global comp_guess
    comp_guess = random.randint(1, 10)


def number_input():
    global player_num
    player_num == input("guess a number between 1 and 10: ")
    # print(player_num)
    return player_num


def number_return():
    print(player_num)
    print(comp_guess)
    return player_num


def compare_guess():
    global game_status
    if player_num > comp_guess:
        print("Too High")
    elif player_num < comp_guess:
        print("Too Low")
    else:
        print("Correct!!")
        game_status = False


def play_again():
    global game_status
    choice = input("do you want to keep playing? (Y/N) ")
    if choice.lower == 'y':
        game_status = True
        game()
    else:
        game_status = False


def game():
    global game_status
    while game_status:
        number_input()
        compare_guess()
        number_return()
        play_again()


def main():
    """main function"""
    game()
    # number_input()
    # number_return()


if __name__ == '__main__':
    main()
