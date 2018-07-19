 get the user to guess a number
# guess_number = int(input("Guess a number from 1-10: "))

# # check if the number is equal to the actual number

# #is the number is correct desply a correct fuess message

# if guess_number <5:
#     print("Please guess higher")
#     if guess_number ==5:
#         print("well done you guessed it correctly ")
#     else:
#         print("You guessed wrong")

# elif guess_number >5:
#     print("Please guess lower")
#     if guess_number ==5:
#         print("welcome you guessed it correctly")
#     else:
#         print ("You guessed wrong")

# else:
#     print ("Well done you guessed it correctly the first time")

#Testing Program control flow
# get user name
# get user age
# check if age is greater than 18
# check if user age is greater than 18 and display this message"Buhari for 2019"
# else if the age is less than 18 substract the age from 18 and display a message "come back in XXXX years"

# voter_name = (input("Hi, what is your name:"))
# voter_age = int(input("what is your age {} :".format(voter_name)))
# if (voter_age < 18) and (voter_age<60):
#     print("Come back {0} in {1} years". format(voter_name, 18-voter_age))
# else voter_age >=18:
#         print("You are eligeable to vote, Buhari for 2019 {} ".format(voter_name))


name = (input("Hi, what is your name:"))
age = int(input("what is your age {} :".format(name)))
if (age <= 18) and (60 >= age):
    print("Have a nice day at work{}".format(name))
elif 18 > age:
	print("Hi {} you are too young to work".format(name))
else:
	print("Hi, {} please reitre".format(name))
