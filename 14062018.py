# which line is not correct?
print("Python was created by Guido van Rossum")
print("He's referred to as the BDFL,")
#print("the "Benovolent Dictator For Life"")
print("and has the final word when it comes to enhancements to Python.")
print("."*45)

#2. In this program, 2 of the variables will have the same value
meal1 ="spam" + "eggs" + "beans"
meal2= "spam\neggs\nbeans"
meal3="spam, eggs, beans"
meal4="""spam eggs beans"""
print(meal1)
print(meal2)
print(meal3)
print(meal4)
print("."*45)

#3. What will be the output produced by this line? 
print ("Terry\tGraham\tMichael\tTerry")

# 4. what will be the output produced this program ?

first_Name = "Gina"
last_name = "Cleese"
age = '78'
print (first_Name + " " +  last_name + " " + age)

# 5. what result will this program print?
a=45
b=15
c=3
print(a-b/c)

print("."*45)
"""6. A banker earns a sum of 5,000 monthly pays tax of 5% of his totla salary at 
the end of the month. write a programto determine how much he will be left with
at the end of the month after tax 
Note: Please declare all your variables clearly """
mon_salary= 5000
tax_rate = 0.05
income_tax= mon_salary*tax_rate
amount_left= mon_salary- income_tax
print(amount_left)
print("."*45)

# sicing and formatiing-variables
parrot="Norwegian Blue"
print(parrot[0:3])
print(len(parrot))
print(parrot[0:6])
print(parrot[0:9:2])
print(parrot[-1])
print(parrot[-1:-15:-1])
# reverse printing with slicing and formatting
virtue = "kind"
print(virtue[-1:-5:-1])
print(len(virtue))
print("."*45)
# slicing and stepping
print(parrot[-6:-1:2])
print(parrot[6:30])
print(parrot[0:30])
print(parrot[0:20:2])

sub_string_parrot1 = parrot[0:9]
sub_string_parrot2 = parrot[10:] 

print("."*45)
#slice till the end 
print(sub_string_parrot1 + " "+ sub_string_parrot2)

print("."*45)
# slicing methods
apple = "Important Notification"
print(apple[0:5]) #start and end
print(apple[3:12:]) #start and end 
print(apple[0:12:3]) # start, end and step 
print(apple[ 0::5]) #star, no end and step
print(apple[::2])# no start, no end and step
print(apple[0:: ]) #start, no end, no step
print(apple[::])# no start, no end, no step
print(apple[:])

print("."*45)
#formatting and replacement fields
first_Name = "Alexander"
last_name = "Mikky"
age =45
type_of_food= "Fried rice and rosted Chicken"
print("My name is {0} {1} and i am {2} years old and i like {3}".format(first_Name,last_name,age,type_of_food))

MyString = "abcde"
print(MyString[-1:-7:-1])
print(MyString[-1:-15:-1]) # line 95 & 96 
print(parrot[-1:len(parrot)-1:-1])
print("."*45)

"""Program flow control in Python
 Program control using conditional statement in Python 
congratulatoryMessage = "Hurry you were successful"
rejection_message = "sorry try again next year"
age =  input("How old are you: ")

if int(age) >= 18:
 print(congratulatoryMessage)
else:
 	print(rejection_message)


greeting = "Hello"
name = input("Please enter your name:")
if name != '':
	print(greeting + name)
else:"""
a=12
b=5
if a % b > 3:
	print(True)
elif a % b == 2:
	print("This is the correct answer")
else:
	print(False)
