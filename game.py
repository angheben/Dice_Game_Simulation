import pandas as pd
import classes
from random import randint

control = {}

name_1 = input("Type the name of the first player: \n"
               "-> ")
name_2 = input("Type the name of the second player: \n"
               "-> ")
player_1 = classes.Player(name=name_1)
player_2 = classes.Player(name=name_2)


def menu():
    answer_1 = int(input("Chose one of the options bellow:\n"
                         "1) See the score;\n"
                         "2) Play a round;\n"
                         "3) End game;\n"
                         "-> "))
    while answer_1 != 1 or 2 or 3:
        if answer_1 == 1:
            see_the_score()
        elif answer_1 == 2:
            play_a_round()
        elif answer_1 == 3:
            print("Tks for play!")
            pass
        else:

            print('Invalid Option')
            break
        break

def see_the_score():
    control[name_1] = [player_1.score]
    control[name_2] = [player_2.score]
    control_df = pd.DataFrame(control)
    print(control_df)
    menu()


def play_a_round():
    answer_1 = input(f"{player_1.name} do you want to throw the dice? (Yes/No)\n"
                     f"-> ")
    if answer_1.lower() == 'yes':
        dice_result_1 = randint(1, 6)
        print(f"Your dice resulted in {dice_result_1}")
    else:
        dice_result_1 = 0
    answer_2 = input(f"{player_2.name} do you want to throw the dice? (Yes/No)\n"
                     f"-> ")
    if answer_2.lower() == 'yes':
        dice_result_2 = randint(1, 6)
        print(f"Your dice resulted in {dice_result_2}")
    else:
        dice_result_2 = 0
    if dice_result_1 > dice_result_2:
        player_1.score += 1
    elif dice_result_1 < dice_result_2:
        player_2.score += 1
    else:
        print("The dice values resulted the same, no score increase for both players")
    menu()


menu()
