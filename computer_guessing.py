from random import random
from time import clock

rand_val = random()
start_time = clock()
upper_bound, lower_bound = 1.0, 0.0
is_guessed = False
guess = 0.5
while is_guessed ==False:
    guess = (upper_bound + lower_bound)/2
    if guess == rand_val:
        print("Number has been found: ", guess)
        print("Time taken: ", (clock() - start_time))
        is_guessed = True
    elif guess < rand_val:
        lower_bound = guess
    else:
        upper_bound = guess