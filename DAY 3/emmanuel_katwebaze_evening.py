 # DAY 3
# Individual Assignment
# Exercise1 (Lists)
print("*************************** EXERCISE 1 ********************************")
# 1. Create a list with 5 items (names of people) and write a python program to output the 2nd
# item.

people = ['Emma', 'John', 'Maria', 'Daniel', 'Luke']
print('The second item is', people[1])

# 2. Write a python program to change the value of the first item to a new value
people[0] = 'Jerry'
print(people)

# 3. Write a python program to add a sixth item to the list
people.append('Jax')
print(people)

# 4. Write a python program to add “Bathel” as the 3rd item in your list
people.insert(2, "Bathel")
print(people)

# 5. Write a python program to remove the 4th item from the list
people.pop(3)
print(people)

# 6. Use negative indexing to print the last item in your list
print('The last item in the list is', people[-1])

# 7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.

fruits = ['mangoes', 'guavas', 'oranges', 'bananas', 'watermelons', 'apples', 'berries']
for i in range(2, 5):
    print(fruits[i])

# 8. Write a list of countries and make a copy of it.
countries = ['Uganda', 'Canada', 'USA', 'Kenya']
list_copy = countries.copy()
print(list_copy) 

# 9. Write a python program to loop through the list of countries
for country in countries:
    print(country)

# 10. Write a list of animal names and sort them in both descending and ascending order.
animals_list = ["horse", "cat", "dog", "lion", "zebra"]
print(animals_list)
print('Sorting in ascending order:')
animals_list.sort()
print(animals_list)

print('Sorting in descending order:')
animals_list.sort(reverse=True)
print(animals_list)

# 11. Using the list above, write a python program to output only animal names with the letter 
# ‘a’ in them
for animal in animals_list:
    if 'a' in animal:
        print(animal)
        
# 12. Write two lists, one containing your first names and the other your second names. Join 
# the two lists.
first_name = ['Emma']
second_name = ['Katwebaze']

combined_names = first_name + second_name
print(combined_names)

# Exercise2 (Tuples)
print("*************************** EXERCISE 2 ********************************")
# 1. Consider the tuple below;
# x = (“samsung”, “iphone”, “tecno”, “redmi”)
# Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
print("My favorite phone brand is", x[0])

# 2. Use negative indexing to print the 2nd last item in your tuple.
print('The second last item in the tuple is', x[-2])
 
# 3. Using the phones list above, write a python program to update “iphone” to “itel”
# Convert the tuple to a list
phone_list = list(x)

# Find the index of "iphone"
index = phone_list.index("iphone")

# Update the value at the specified index
phone_list[index] = "itel"

# Convert the list back to a tuple
phone_list = tuple(phone_list)

print("Updating iphone to itel results in", phone_list)
# 4. Write a python program to add “Huawei” to your tuple.
new_phone = "Huawei"

# Create a new tuple by concatenating the existing tuple with the new element
x += (new_phone,)
print("The updated tuple is", x)

# 5. Write a python program to loop through the tuple above.
for phone in x:
    print(phone)

# 6. Write a python program to remove/delete the first item in your tuple.
x_list = list(x)

del x_list[0]

updated_phones = tuple(x_list)

print("The updated phones tuple is", updated_phones)


# 7. Using the tuple() constructor, create a tuple of the cities in Uganda.
uganda_cities = tuple(['Kampala', 'Jinja', 'Gulu', 'Lira', 'Mbarara', 'Mbale', 'Entebbe'])
print(uganda_cities)

# 8. Write a python program to unpack your tuple.
# Unpack the tuple into individual variables
city1, city2, city3, city4, city5, city6, city7 = uganda_cities

# Print the unpacked variables
print(city1)
print(city2)
print(city3)
print(city4)
print(city5)
print(city6)
print(city7)

# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
print("Second, Third and 4th cities are:")
for i in range(1,4):
    print(uganda_cities[i])

# 10. Write two tuples, one containing your first names and the other your second names. Join 
# the two tuples.
first_name = ("Emma",)
last_name = ("Katwebaze",)

# Join the two tuples
full_name = first_name + last_name

print(full_name)

# 11. Create a tuple of colors and multiply it by 3.
colors = ("red", "green", "blue")
multiplied_colors = colors * 3

print(multiplied_colors)

# 12. Return the number of times 8 appears in this tuple this tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
numbers_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
eight_count = numbers_tuple.count(8)

print("8 appears", eight_count, "times")

# Exercise3 (Sets)
print("*************************** EXERCISE 3 ********************************")
# 1. Use the set() constructor to create a set of 3 of your favorite beverages.
fav_beverages = set(["coffee", "tea", "juice"])

print(fav_beverages)

# 2. Use the correct method to add 2 more items to the beverages set.
fav_beverages.add("soda")
fav_beverages.add("water")
print(fav_beverages)

# 3. Given the set below;
# mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
# Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print(mySet)
if "microwave" in mySet:
    print("microwave is in the set")
else:
    print("microwave is in the set")

# 4. Write a python program to remove “kettle” from the set above.
mySet_copy = mySet.copy()
mySet_copy.remove("kettle")
print(mySet_copy)

# 5. Write a python program to loop through the set above.
for item in mySet:
    print(item)

# 6. Write a set of 4 items and a list of two items. Write a python program to add elements in 
# the list to elements in the set.
item_set = {"apple", "banana", "orange", "grape"}
item_list = ["pineapple", "watermelon"]

# Adding elements from the list to the set
item_set.update(item_list)

print(item_set)


# 7. Write two sets, one containing your ages and the other your first names. Join the two 
# sets.
ages = {25, 60, 35}
first_names = {"Jon", "Emma", "Franky"}

# Joining the two sets
combined_set = ages.union(first_names)

print(combined_set)


# Exercise4 (Strings)
print("*************************** EXERCISE 4********************************")
# 1. Declare two variables, an integer and a string and use the correct method to concatenate 
# the two variables.
my_int = 25
my_string = "Hello"
concatenated_variable = str(my_int) + my_string
print(concatenated_variable)


# 2. Consider the example below;
# txt = “ Hello, Uganda! ”
# Output the string without spaces at the beginning, in the middle and at the end.
txt = " Hello, Uganda! "
txt = txt.strip()
txt = txt.replace(" ", "")
print(txt)

# 3. Write a python program to convert the value of ‘txt’ to uppercase.
txt_uppercase = txt.upper()
print(txt_uppercase)

# 4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
updated_txt = txt.replace('U', 'V')

print(updated_txt)

# 5. Using the code below, write a python program to return a range of characters in the 2nd
# ,3rd and 4th position.
# y = “I am proudly Ugandan”
y = "I am proudly Ugandan"    
character_range = y[1:4]

print(character_range)

# 6. The piece of code below will give an error when output;
# x = “All “Data Scientists” are cool!” 
# Write a python program to correct it.
x = 'All "Data Scientists" are cool!'
print(x)

#OR
x = "All \"Data Scientists\" are cool!"
print(x)

# Exercise5 (Dictionaries)
print("*************************** EXERCISE 5 ********************************")
# 1. With reference to the dictionary below, write a python program to print the value of the 
# shoe size. 
# Add this dictionary to your .py file
# Shoes = {
# “brand” : “Nick”,
# “color” : “black”,
# “size” : 40
# }

Shoes = {
"brand": "Nick",
"color" : "black",
"size" : 40
}

print("The shoe size is", Shoes["size"])


# 2. Write a python program to change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print("The updated dictionary is", Shoes)



# 3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print("The updated dictionary is", Shoes)

# 4. Write a python program to return a list of all the keys in the dictionary above.
keys_list = list(Shoes.keys())
print("The dictionary keys are", keys_list)


# 5. Write a python program to return a list of all the values in the dictionary above.
values_list = list(Shoes.values())
print("The dictionary values are", values_list)

# 6. Check if the key “size” exists in the dictionary above.
if "size" in Shoes:
    print("size is in the dictionary")
else:
    print("size is not in the dictionary")

# 7. Write a python program to loop through the dictionary above.
for key, value in Shoes.items():
    print(key, ":", value)  
    
# 8. Write a python program to remove “color” from the dictionary.
del Shoes["color"]
print(Shoes)

# 9. Write a python program to empty the dictionary above.
Shoes.clear()

print(Shoes)


# 10. Write a dictionary of your choice and make a copy of it.
dict = {
    "name": "Jax",
    "age": 30,
    "city": "New York"
}
print(dict)
dict_copy = dict.copy()

print(dict_copy)

# 11. Write a python program to show nested dictionaries
dicts_nested = {
    "person1": {
        "name": "Jax",
        "age": 30,
        "city": "New York"
    },
    "person2": {
        "name": "Jons",
        "age": 22,
        "city": "London"
    }
}
print(dicts_nested)
# Accessing values in the nested dictionaries
print("name: ", dicts_nested["person1"]["name"] + ", age:", dicts_nested["person1"]["age"])
print("name: ", dicts_nested["person2"]["name"] + ", age:", dicts_nested["person2"]["age"])

#OR
for person, details in dicts_nested.items():
    print("Person:", person)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("City:", details["city"])
    print()


