# def stupid_addition(a,b):
#     if type(a) == int:
#         if type(b) == int:
#             return str(a) + str(b)
#         else:
#             return None
#     if type(a) == str:
#         if type(b) == str:
#             return int(a) + int(b)
#         else:
#             return None
"""
Future: 
- might look at a different logic for replaying vs playing for the first time
-collect user input about the game settings(min, max of random number, munber of guesses allowed, etc)

Planning: 

"""

import random

is_playing = True

while is_playing:
    print("Welcome to Guess the  Number! I hope you have fun")
    number_to_guess = random.randint(1, 100)
    correct_guess = False

    while not correct_guess:
        user_guess = int(input(
            "I'm thinking of a number between 1 and 100. Guess which number I'm thinking of: "))
        # TODO: provide data to the user about the game(like number of guesses so far)
        # TODO: do some error checking on user input

        if user_guess == number_to_guess:
            correct_guess = True
            print("Congradulations you Won!")
            play_again = input("Would you like to play again? Y or N?")
            if play_again.lower() == 'n':
                is_playing = False

        elif user_guess > number_to_guess:
            print("The guess was too high")
        else:
            print('The guess was too low')
