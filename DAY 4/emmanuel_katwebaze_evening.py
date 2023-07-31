# FUNCTIONS
# They group blocks of code
# There is need for code that is clean, reusable and maintainable
# def function_name():
#   # block of code

def afternoon():
    print("Class starts at 2pm")
    print("Attendees are close to 100")


# Calling a function
afternoon()

# Arguments and Parameters
# Parameters are placeholder variables specified in the function signature
# Arguments are variables or items passed to the function during a function call


def add(a, b):
    return a + b


print(add(1, 2))


def names(first_name, last_name):
    print(f"My first name is {first_name} and my last name is {last_name}")


names("Emma", "Katwebaze")


def get_total(*args):
    sum = 0
    for item in args:
        sum += item
    return sum
        
total = get_total(100, 300, 400)
print("The total is", total)

#Function with default values

def greet(greeting="Hi"):
    print(f"{greeting}, how are you?")
    
greet("Hello") # Hello, how are you?
greet() # prints Hi, how are you?

# MODULES
# A simple calc
def add(num1, num2):
    return (num1 + num2)

def product(num1, num2):
    return (num1 * num2)

# importing square root and factorial from the module math
from math import sqrt, factorial
# from math import * 

print(sqrt(16))
print(factorial(10))

# Input and Output in python
# input('prompt')

# Example of input

name = input("Enter your name: ")
print("My name is, " + name)


# Example 2

number = int(input("Enter a value: "))

product = number * 10

print(product)

# Multiple inputs in python

s, r, w = map(int, input("Enter the Values : ").split())
print("The values are : ", end = "")
print(s, r, w)

# How to capture input from a tuple
w = (2, 4, 6, 5, 8)
print("Current tuple", w)

E = list(w)
E.append(int(input("Enter new value: ")))
W = tuple(E)
print("Updated tuple", W)

set_fruit_items = {"mangoes", "apples", "cherries"}
print("Current fruit items:", set_fruit_items)
set_fruit_items.add(input("Enter new item to add to the fruit items: "))
print("Updated fruit items:", set_fruit_items)

mylist = list(map(int, input("Enter the list values: ").split()))
myset = set(map(int, input("Enter the set values: ").split()))

print(mylist)
print(myset)