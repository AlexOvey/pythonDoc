# this application will mimmick user login and registration 
# create a folder in your desktop name in registration
# create a python file in the smae folder and call it register.py

def register():
        #get the user details
        username = input("Enter your username: ")
        while (len(username) < 2):
            username = input("Enter your username greater than two characters: ")


        email = input("Enter your email: ")
        while '@' and '.com' not in email:
            email = input("Please enter a valid email: ")

        password = input("Enter your password: ")
        while (len(password) < 6):
            password = input("Password too short. Enter new password: ")
        # for i in password:
        # 	if i in name:
        # 		password = ('password should not contain any character in name\n Enter again :')

        confirm_password = input("Please confirm your password: ")
        while confirm_password != password:
            confirm_password = input("Password don't match, try again: ")

        gender = input("Select gender (M/F): ").lower()
        #while gender != 'm' or 'f':
        if gender == 'm':
            gender = "Male"
        else:
            gender = "Female"



        # TODO
        # Check that the user has supplied all the correct details such as;
        # "@" sign should be in the email
        # the username should be more than two letters
        # the passwords must match
        # the password must be more than six characters in length

        # write the user details to a file like this

        f = open("userInformation.txt", "a")
        f.write(f"\n{username}, {email},{password},{confirm_password},{gender}")
        f.close( )

        return True

register()

def login():
		# TODO
		# get the email 
		# get the password
		# check if the username and password match a line in your dummy-database
		# print welcome message if there is a match
		# else print a invalid details supplied message
		
		name = username.register()
		email = email.register()
		
		fileToRead = open('userInformation.txt', 'r')

		for info in fileToRead:
			if name and email in info:
				print('yes')
				break
			else:
				print('no')

		fileToRead.close()
		return True
login()


import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        