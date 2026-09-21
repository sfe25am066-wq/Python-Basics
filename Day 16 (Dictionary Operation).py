#Create a dictionary
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red"
}
#Print the dictionary
print(fruit_colors)
#Accessing elements in a dictionary
print("Color of apple:", fruit_colors["apple"])
#Adding a new key-value pair to the dictionary
fruit_colors["date"] = "brown"
print("Updated dictionary:", fruit_colors)
#Removing a key-value pair from the dictionary
del fruit_colors["banana"]
print("Dictionary after removing banana:", fruit_colors)
#Updating a value in the dictionary
fruit_colors["cherry"] = "dark red"
print("Updated color of cherry:", fruit_colors["cherry"])
#Getting all keys and values from the dictionary
keys = fruit_colors.keys()
print("All fruits:", list(keys))
#Getting all values from the dictionary
values = fruit_colors.values()
print("All colors:", list(values))
#Dictionary comparison
another_fruit_colors = {
    "apple": "red",
    "cherry": "dark red",
    "date": "brown"
}
print("Another fruit colors:", another_fruit_colors)

