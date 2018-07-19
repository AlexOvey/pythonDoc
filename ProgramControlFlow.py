# guessing the number game

# get the user to guess a number
guess_number = int(input("Guess a number between 1-10: "))



# check if the number is equal to the actual number
if guess_number < 5:
    print("Please guess higher")
    guess_number = int(input("Guess a number between 1-10: "))
    if guess_number == 5:
        print("Weldone you guessed it correctly the first time")
    else:
        print("You guessed wrong")
elif guess_number > 5:
    print("Please guess lower")
    guess_number = int(input("Guess a number between 1-10: "))
    if guess_number == 5:
        print("Weldone you guessed it correctly")
    else:
        print("You guessed wrong")

else:
    print("Weldone you guessed it correctly the first time")
# if the number is correct display a correct guess message
# else display a wrong message
