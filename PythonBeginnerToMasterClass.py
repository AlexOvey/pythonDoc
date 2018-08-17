list_1 = [2,4,6,7,8,9,0,19]
list_2 = [2,3,4,5,6,89,8,]
list_3 = list()

list_1.append(1)
list_1.append("name")
list_1.insert(0, 'Isaish')
print(list_1)
list_4 = list_1 + list_2 + list_3
for i in list_4:
	print(i, end = ' ')