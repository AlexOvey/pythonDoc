import csv
import math
import android


#list is defined as a homogenous group of items although
#in practice homogenity is not actually enforced

#to create
# list_1 = [] #list literal
# list_2 = list()  #list function


# #to create a list of string and items to it
# list_1.append("eggs")
# list_1.append("spam")
# list_1.append("milk")
# list_1.append("bacon")
# list_1.append("cheese")
# list_1.append("butter")
#
# list_1= ['egg','spam','milk']
# for item in list_1:
#     print(f"The item position is {list_1.index(item)} and the item name is {item}")
# print(len(list_1))#to get the length of a list
# print(list_1[0])#to get an item in a list
# print(list_1.index('spam'))#to get the position of an item in a list
# list_1[2] = 'groundnut'
# print(list_1)
# del list_1[1]
# print(list_1)
# for item in list_1: # to iterate through a list
#     print('The item position is {} and the item is {}'.format(list_1.index(item),item))
#
# list_2.append(2)
# list_2.append(4)
# list_2.append(6)
# list_2.append(8)
# list_2.append(10)
#
# list_2=[2,4,6,8,10]


# list_3=list(range(1,10,2))
# list_4=list(range(2,10,2))
# #print(list_3)
# numbers = list_2 + list_3
# numbers.sort() # arranges the list in ascending order
# print(numbers)


# print(list_1)
# print(list_2)

# menu = [
#             ['egg', 'butter', 'bacon'],
#             ['egg', 'cheese', 'bacon', 'beef'],
#             ['egg', 'spam', 'spam', 'bacon'],
#             ['egg', 'spam', 'spam', 'spam', 'spam',  'bacon', 'cheese'],
#             ['egg', 'spam'],
#             ['egg', 'egg', 'bacon', 'cheese'],
#         ]
# # print list without spam
# for meal in menu:
#     if 'spam' in meal:
#         continue
    # else:
    #     print(meal)
# printlist with spam
    # for ingredient in meal:
    #     print(ingredient)

# for meal in menu:
#     if 'bacon' in meal:
#         continue
#     else:
#         print(meal)

#list equality
# if list_2 == list_3:
#     print(True)
# else:
#     print(False)
#
# if list_2 > list_4:
#     print(True)
# else:
#     print(False)

#CREATING A DYNAMIC LIST
# sevens  = list()#list of numbers that are multiples of 7
# eights = []#list of numbes that are multiples of 8
#
# first_100_number = list(range(1, 101))
# # print(first_100_number)

# for num in first_100_number:
#     if num % 7 == 0:
#         sevens.append(num)
#     elif num % 8 == 0:
#         eights.append(num)
#     else:
#         continue
# print(sevens)
# print(eights)

#Challenges
#create a list of all even numbers from 2 - 50
# create a list of all odd numbers from 1-50
# iterate through the list of even numbers and find their sum
# iterate through the list of odd numbers and find their sum
# (HINT: do research on the internet for this)
# from the menu list above write a program to print out list without 'bacon'

# list_1 = list(range(2,51,2))
# list_2 = list(range(1,50,2))
# sum=0
#
# for i in list_1:
#     sum += i
# print(sum)
#
# for i in list_2:
#     sum+=i
# print(sum)

#it can be done this way too
# sum_even_numbers_list = sum(list_1)
# print(sum_even_numbers_list)


# 17-07-2018

"""
    challenge is to sort a list and print the reverse order
    class challenge: create a list of ten books you know, sort them in their correct order
    loop through the books and print put the book name and index
""" 

# list_5 = ['gifted hand', 'six feet from gold','how to thick','thinkand grow rich','Earth to centuari',\
#  'The Klahlar files','The wosnik tunnel' ]
# list_5.sort()
# print(list_5)
# for book in list_5:
#     print(f"The book index is {list_5.index(book)} and the book name is {book})")
# list_6 = list(range(1,10,2))
# list_7 = list(range(2,10,2))
# numbers = list_6 + list_7
# numbers.sort()
# print(numbers)

# checking equality of a list
# tens = []
# eights = []
# fives = []
# first_100_number = list(range(1,101))
# for num in first_100_number:
#    if num % 10 == 0:
#     tens.append(num)
#     continue
# for num in first_100_number:
#     if num % 8 ==0:
#        eights.append(num)
#     continue
# for num in first_100_number:
#     if num % 5 == 0:
#         fives.append(num)
#     continue
# print(fives)
# print(eights)
# print(tens)

# common_elements = []
# for number in tens:
#     if (number in eights) and (number in fives):
#         common_elements.append(number)
# print(common_elements)

""" 
    from our list of list

"""

# for ingredient in menu:
#     if 'spam' in ingredient:
#         print(ingredient)
#     else:
#         continue

# Tuples is defined as a heterogenous group of items although 
# in practice heterogenity is not actually enforced

# to create a tuple
# tuple_1 = () # tuple literal
# tuple_2 = tuple() # tuple method

# # tuples are immutable
# print(tuple_1)
# print(tuple_2)

# # tuples inside tuples 
# tuple_3 = (
#     ("Olamide","who you epp", 2016),
#     ("Tiwa savage", "badd",2014),
#     ("Davido", "Fia", 2017),
#     ("kiss Daniel", "no do", 2018)
#     )
# unpacking with tuples
# for item in tuple_3:
#     name, title, year = item
#     print(f"Artist:{name}, Song title: {title}, year:{year}")

# for item in tuple_3:
#     print(item)
# flightfile = open("flights.csv")
# reader = csv.reader(flightfile)  
# for item in reader:
#         origin, destination, duration = item
#         print(f"Origin:{origin}, destination: {destination}, duration:{duration}")

# def main():
#     webUrl = urllib.request.urlopen("http://www.google.com")
#     print("result code: " + str(webUrl.getcode()))
#     data = webUrl.read

#     if __name__== "__main__":
#         run.main()

# dict_1= {'name':'zara','age':7,'class':'first'}
# print(dict_1['name'])
# print(dict_1['age'])

# nums = set([1,2,2,3,4,5,6])
# print(min(nums))
# print(max(nums))
# print(len(nums))

# a = [1,1,2,2,2,3,3,4,4]
# b = set(a)
# def test(lst):
#     if lst in b:
#         return 1
#     else:
#         return 0
#     pass

