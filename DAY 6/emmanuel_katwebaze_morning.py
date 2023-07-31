# DAY 6
# Advanced topics in Python

"""
* Regular expressions
* Generators and iterators
* Decorators 
* Context managers
* Multithreading and multiprocessing

# Regular Expressions
summary:

\d : Matches any digit (0-9)
\w: Matches any alphanumeric character (a-z, A-Z, 0-9, and underscore)
\s: Matches any whitespace character (space, tab, newline)
. : Matches any character except a newline
* : Matches zero or more occurrences of the preceding character or group
+ : Matches one or more occurrences of the preceding character or group
? : Matches zero or one occurrences of the preceding character or group
[ ] : Matches any character within the square brackets.
[^ ] : Matches any character not within the square brackets
^ : Matches the start of a line.
$ : Matches the end of a line.

"""
# Matching and Searching
# regex re.match(), re.search(), re.findall()

# Example One
# regex re.match(), re.search(), re.findall()

# Example1 Demonstrating regex | Match First Word, Match Group word, Match All Numbers

import re
text = "Hello, my name is Emma. I am a programmer with 15 years of experience"

# Match First Word
match = re.search(r"^\w+", text)

if match:
    print("Match:", match.group())

match1 = re.search(r"\w+$", text)

if match1:
    print("Match1:", match1.group())


matches = re.findall(r"\d+", text)

if matches:
    print("Matches:", matches)

pattern = "Emma"
match2 = re.search(pattern, text)

if match2:
    print("Match2:", match2.group())

# Example2 validate email format or email address


def validate_email(email):
    pattern = r"^[\w+\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return "Valid email address"
    else:
        return "Invalid email address"


# Example usage
print(validate_email("emma@gmail.com"))
print(validate_email("emmagmail.com"))
print(validate_email("emm.a@gmail.com"))
print(validate_email("12343445"))

# Other examples
# Ex1
pattern = r"[,;]"
text = "apple,banana;cherry"

splits = re.split(pattern, text)
print(splits)

# Ex2
pattern = r"apple"
text = "I like apple."

new_text = re.sub(pattern, "orange", text)
print(new_text)

pattern = r"(\d{2})-(\d{2})-(\d{4})"
text = "Date: 01-23-2023"

match = re.search(pattern, text)
if match:
    day = match.group(1)
    month = match.group(2)
    year = match.group(3)
    print(f"Day: {day}, Month: {month}, Year: {year}")
    
# Ex3
import re

def validate_password(password):
    # Password criteria: 
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one digit
    # - Contains at least one special character (!@#$%^&*)

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"
    match = re.match(pattern, password)

    if match:
        return True
    else:
        return False

# Testing the password validation function
password1 = "Abc123!$"
password2 = "password"
password3 = "weak"
password4 = "Passw0rd"

print(validate_password(password1))  # Output: True
print(validate_password(password2))  # Output: False
print(validate_password(password3))  # Output: False
print(validate_password(password4))  # Output: False
"""
(?=...) : construct is known as a positive lookahead. It is a non-capturing group that asserts a 
condition without including it in the final match. 
The ... inside the lookahead represents the condition 
that needs to be satisfied.

(?=.*[a-z]) checks if the password contains at least one lowercase letter.
(?=.*[A-Z]) checks if the password contains at least one uppercase letter.
(?=.*\d) checks if the password contains at least one digit.
(?=.*[!@#$%^&*]) checks if the password contains at least one special character from the specified set.
.{8,} ensures that the password is at least 8 characters long.

"""

# Generators and Iterators
# 'yield' generator
# Iterator '__iter__'  "__next__" iterator


def factorial(n):
    # return the factorial of a number
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Print the factorial of a range of numbers from n to m using a generator
def factorial_generator(n, m):
    for i in range(n, m):
        yield factorial(i)


# Example usage
for factorial_value in factorial_generator(1, 10):
    print(factorial_value)


def factorial(n):
    # return the factorial of a number
    if n == 0 or n == 1:
        yield 1
    else:
        fact = 1
        for i in range(1, n):
            fact *= i
        yield fact


for i in range(1, 6):
    print(*factorial(i))

# Example 3
print("*********** Example 3 ****************")


def squares():
    for i in range(1, 10):
        yield i ** 2

# Create an iterator object that yields the square of numbers from 1-10


squares_iterator = squares()

# Print the first 5

for n in range(5):
    print(next(squares_iterator))


# Decorators @my_decorator
# Decorators in Python allow you to modify the behavior of functions or classes without
# directly changing their source code.

def my_decorator(func):
    def inner():
        print("This is the decorator")
        func()
    return inner


@my_decorator
def outer_decorator():
    print("This is outer decorator")


outer_decorator()

# Example 2


def decorator_function(original_function):
    def wrapper_function():
        print("Before the original function")
        original_function()
        print("After the original function")
    return wrapper_function


@decorator_function
def greet():
    print("Hello, world!")


greet()

# Example 3
def decorator_with_arguments(arg1, arg2):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(f"Decorator arguments: {arg1}, {arg2}")
            original_function(*args, **kwargs)
        return wrapper_function
    return decorator_function


@decorator_with_arguments("arg1 value", "arg2 value")
def greet(name):
    print(f"Hello, {name}!")

greet("Emma")
