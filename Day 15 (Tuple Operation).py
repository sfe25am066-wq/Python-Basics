# Create a tuple
fruits=("apple", "banana", "cherry", "date", "elderberry")
#Print original tuple
print("Original tuple:", fruits)
#Accessing elements in a tuple
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
#Tuple slicing
print("First three fruits:", fruits[0:3])
print("Last two fruits:", fruits[-2:])
# Length of the tuple
length=len(fruits)
print("Length of the tuple is:", length)
#Counting occurrences of an element in a tuple
count=fruits.count("banana")
print("Count of 'banana' in the tuple is:", count)
#Find index of an element in a tuple
index=fruits.index("cherry")
print("Index of 'cherry' in the tuple is:", index)
# Tuple unpacking
a, b, c, d, e = fruits
print("Unpacked fruits:", a, b, c, d, e)
#Nested tuple
nested_tuple=(1, 2, (3, 4), 5)
print("Nested tuple:", nested_tuple)
print("Inner tuple:", nested_tuple[2])
#Tuple concatenation
more_fruits=("fig", "grape")
combined_fruits=fruits + more_fruits
print("Combined tuple:", combined_fruits)
#Tuple repetition
repeated_fruits=fruits * 2
print("Repeated tuple:", repeated_fruits)
#Tuple comparison
tuple1=(1, 2, 3)
tuple2=(1, 2, 4)
print("tuple1 < tuple2:", tuple1 < tuple2)