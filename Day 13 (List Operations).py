#Initialise a list
Fruits=["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(Fruits)
#Add one item to the list
Fruits.append("Pineapple")
print(Fruits)
#Remove one item from the list
Fruits.remove("Banana")
print(Fruits)
#Access item from list using index
print(Fruits[2])
print(Fruits[0])
#Slice the list
print(Fruits[1:4])
#Find the index of an item in the list
print(Fruits.index("Mango"))
#Count the number of occurrences of an item in the list
print(Fruits.count("Apple"))
#Sort the list in ascending order
Fruits.sort()
print(Fruits)
#Reverse the list
Fruits.reverse()
print(Fruits) 
