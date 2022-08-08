from random import random

rand_val = random()

upper_bound, lower_bound = 1.0, 0.0
is_guessed = False
guess = 0.5
while is_guessed ==False:
    if guess == rand_val:
        print("Number has been found: ", guess)
        is_guessed = True
    elif guess < rand_val:
        lower_bound = guess
    else:
        upper_bound = guess
    guess = (upper_bound + lower_bound)/2