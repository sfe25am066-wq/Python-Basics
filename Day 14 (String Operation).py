str="Hello, World!"
length=len(str)
print("Length of the string is:", length)
#Uppercase the string
upper_str=str.upper()
print("Uppercase string is:", upper_str)
#Lowercase the string
lower_str=str.lower()
print("Lowercase string is:", lower_str)
#Capitalize the string
capitalized_str=str.capitalize()
print("Capitalized string is:", capitalized_str)
# Replace a substring in the string
replaced_str=str.replace("World", "Python")
print("Replaced string is:", replaced_str)
# Split the string into a list of substrings
split_str=str.split(",")
print("Split string is:", split_str)
#Join a list of substrings into a single string
joined_str=" ".join(split_str)
print("Joined string is:", joined_str)
#Index of a string
index=str.index("r")
print("Index of 'r' in the string is:", index)
