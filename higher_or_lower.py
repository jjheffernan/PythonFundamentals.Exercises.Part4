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
    return comp_guess


def number_input():
    global player_num
    player_num = int(input("guess a number between 1 and 10: "))
    # print(player_num)
    return player_num


def number_return():
    pass
    # print(player_num)
    # print(comp_guess)
    # return player_num


def compare_guess():
    global game_status
    global player_num
    global comp_guess
    # player_choice = player_num
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
    if choice == 'n':
        game_status = False

    elif choice == 'y':
        game_status = True

    else:
        print("Error!")


def game():
    global game_status
    global player_num
    global comp_guess
    while game_status:
        # print(comp_guess)
        player_num = number_input()

        compare_guess()
        number_return()
        if game_status:
            play_again()

        # choice = input("do you want to keep playing? (Y/N) ")
        # if choice == 'n':
        #     game_status = False
        # elif choice == 'y':
        #     game_status = True
        #     game()
        # else:
        #     print("Error!")


def main():
    """main function"""
    global comp_guess
    comp_guess = computer_guess()
    game()
    # number_input()
    # number_return()


if __name__ == '__main__':
    main()
