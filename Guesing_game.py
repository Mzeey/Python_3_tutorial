from random import randint

rand_val = randint(1, 100)
is_guessed = False

while is_guessed == False:
    guess = input("Please Guess a number. Hint: Range is 1 to 100: ")
    guess = int(guess)
    if guess == rand_val: 
        is_guessed = True
        print("You guessed correctly. your guess was: ", guess)
    elif guess < rand_val:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
