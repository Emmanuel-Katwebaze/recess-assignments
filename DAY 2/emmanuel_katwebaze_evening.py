#DAY_2
#Dictionaries
#used to store values in key:value pairs
#they are ordered, changeable, but do not allow duplicates
#Dicts can have items of any data type

mydict = {
    "phone": "iphone",
    "iphone_model": "iphone15",
    "year": 2023
}

print(mydict)

#Length of dictionary
print(len(mydict))

#Data type
print(type(mydict))

#Access Dictionary items
z = mydict["year"]
print(z)

y = mydict.get("iphone_model")
print(y)

w = mydict.keys()
print(w)
y = mydict.values()
print(y)

#using dict constructor
mydict2 = dict(name="Emma", age=21, regNo="21/U/06815/PS")
print(mydict2["regNo"])

#copy a dictionary
dict_copy = mydict2.copy()
print(dict_copy["regNo"])

#deleting items from a dictionary
print(dict_copy)
del dict_copy["name"]
print(dict_copy)

dict_copy.popitem()
print(dict_copy)

print("********** EXERCISE ******************")
#Exercise One: use the values () method to return a list of all values in the dictionary
mydict2_values = mydict2.values()
print(mydict2_values)

#Exercise Two: to check if a key does exist in your dictionary
if 'name' in mydict2:
    print("Key 'name' exists in the dictionary")

#Exercise Three: Give an example on how to change dictionary items, How to update
mydict2.update({"name": "Katwebaze"})
print(mydict2) 

#Exercise Four: Give an example on how to add dictionoary items. how to remove dictionary items
mydict2['student_number'] = '21/U/06815/PS'
print(mydict2) 

del mydict2["name"]
print(mydict2)
#Exercise Five: Give an example on how you can loop through a dictionary and also how to nest dictionaries
print("******** Looping through items in dictionary ************")
for key, value in mydict2.items():
    print(key, "-", value)

print("******** Nest items in dictionary ************")
fruits_stock = {
    'apple': {'count': 3, 'price': 1.99},
    'banana': {'count': 5, 'price': 0.99},
    'grape': {'count': 4, 'price': 2.49}
}
print(fruits_stock['apple']['count']) 
print(fruits_stock['banana']['price'])  

print("********** END EXERCISE ******************")
#integers, floats, complex
w = 10 #int
r = 3.9 #float
s = 2j

print(type(w))
print(type(r))
print(type(s))

#integers
a = 2
b = 671212121
c = -56427

print(type(a))
print(type(b))
print(type(c))

#Floats
g = 2.89
z = 3.3
e = -32.29

print(type(g))
print(type(z))
print(type(e))

#Complex numbers
w = 6 + 10j
t = 4j
h = -2j

print(type(w))
print(type(t))
print(type(h))

#Types conversions
w = 10 #int
r = 3.9 #float
s = 2j #complex

#Convert from int to complex
Z = complex(w)
print(z)
print(type(z))

#convert from int to float
number1 = 21
print(f"Type of number1 is: {type(number1)}" )
number1 = float(number1)
print(f"Type of number1 is: {type(number1)}" )
#convert from float to complex
number2 = 21.0
print(f"Type of number2 is: {type(number2)}" )
number2 = complex(number2)
print(f"Type of number2 is: {type(number2)}" )

#convert from complex to float
number3 = 2j
number3 = number3.real
number3 = float(number3)
print(f"Type of number3 is: {type(number3)}" )
number3 = complex(number3)
print(f"Type of number3 is: {type(number3)}" )

#Works mostly when you want to specify a variable type

h = int(20) #h is 20
y = int(3000000000) #y is 300000000
a = int("8") #a is 8
print(h)
print(y)
print(a)
print(type(a))

#Assign string to a variable
w = "Afternoon"
#print(w)
#Multiline strings
q = """I am offering BSSE Year three
 currently doing recess in python, Data Science, Django.
"""

print(q)

#strings as arrays
a = "Afternoon"
print(a[0])

print("********** EXERCISE ******************")
#Exercise one use the len() function to determine the length of your string
fruit = "Bananas"
print(len(fruit))

#Exercise Two Give an example of using a for loop in a string
for letter in fruit:
    print(letter)
    
#Exercise Give an example of slicing in strings
slice1 = fruit[2:]  # Slice from index 2 until the end of the string
print(slice1)  # Output: nanas

slice2 = fruit[:5]  # Slice from the beginning until index 5 (exclusive)
slice4 = fruit[:]  # Slice the entire string (equivalent to fruit)
print(slice2)  # Output: Banan
print(slice4)  # Output: Bananas

slice5 = fruit[::2]  # Slice with a step of 2
print(slice5)  # Output: Bnns


print("********** END EXERCISE ******************")

#How to modify strings
variable2 = "   After noon "
print(variable2.strip())

#string concatenator
c = "Afternoon"
d = "Class"
w = c + d
print(w)
z = c + " " + d
print(z)

#Works when one wants to combine a string to a number
age = 21
name = f"My name is Emma, I am {age}" 
print(name)

#Format argument 
name = "Emma"
age = 21
print("My name is {} and I am {} years old.".format(name, age))

name = "Bob"
age = 30
print("I am {1} years old, My name is {0}.".format(name, age))

name = "Charlie"
age = 35
print("My name is {name} and I am {age} years old.".format(name=name, age=age))
# Output: My name is Charlie and I am 35 years old.

#Exercise Use a condition to show how to use booleans
print("********** EXERCISE ******************")
age = 25
is_adult = age >= 18

if is_adult: #since is_adult evaluates to true
    print("You are an adult.")
else:
    print("You are not an adult.")
    
print("********** END EXERCISE ******************")




