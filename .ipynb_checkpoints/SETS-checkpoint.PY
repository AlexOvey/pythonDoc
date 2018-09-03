# class Program():
# 	def __init__(self, *args, ** kwargs):
# 		self.lang = input('what language?: ')
# 		self.version = input('what version')
# 		self.skill = input("what skill level?")

# p1 = Program()

# # birthdays = {'Alice': 'Apr 1'. 'Bob':'Dec 12', 'Alex': 'Sep 28'}
# # while True:
# # 	print("Enter a name: (blank to quit)")
# # 	name = input()
# # 	if nam == ' '
# # 	break

# # 	if name in birthdays:
# # 		print(f'birthdays[name] + ' is the birthday of ' + name)
# # 	else:
# # 		print(' I do not have birthday information of ' + name)
# # 		print('What is their birthday?')
# # 		bday = input()
# # 		birthdays[] =bday

import matplotlib.pyplot as pt
import pandas as pd
x=[1,3,3,4,5,6,7]
y=[5,-2,4,5,6,9,2]

data = pd.read_csv("temp.csv")
print(data)
# pt.xlabel("X-axis")
# pt.ylabel("y-axis")
# pt.plot(x,y)
# pt.scatter(x,y, color="red")
# pt.title("graph of y against x")
# pt.xlim(-3, 10,1)
# pt.ylim(-3,10,2)
pt.show() 