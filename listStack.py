myStack = []
stackSize = 3

def DisplayStack():
	print("Stack currently contains: ")
	for item in myStack:
		print(item)
	pass
def push(value):
	if len(myStack) < stackSize:
		myStack.append(value)
	else:
		print("Stack is full!")
def Pop():
	if len(myStack) > 0:
		myStack.pop()
	else:
		print("Stack is empty.")
push(1)
push(2)
push(3)
DisplayStack()
input("Press any key when ready...")

push(4)
DisplayStack()
input("Press any key when ready...")

Pop()
DisplayStack()
input("Press any key when ready...")

pop()
pop()
pop()
DisplayStack()
	