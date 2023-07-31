#DAY 3
#Basic Operators and Expressions (Input and Output operators)
"""
Arithmetic Operators
+ Addition
- Subtraction
* Multiplication
/ Division
// Division without remainder
% Modulus
** Exponentiation

# Comparison Operators
== Equal to
!= Not Equal to
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

# Logical Operators
Logical AND: 'and' 
Logical OR: 'or'
Logical NOT: 'not'

# Assignment Operators
Assign value: '='
Add value" '+'
Add and assign value: '+='
Subtract and assign value: '-='
Divide and assign value: '/='
Modulus and assign value: '%='
Exponentiate and assign value: '**='

# Membership operators
In: 'in' operator: checks if a value exists in a sequence
Not in: 'not in' operator: checks if a value dies bit exist in a sequence

# Identity operators
Is: 'is' operator: checks if two values are the same
Is not: 'is not' operator: checks if two values are not the same
"""
# Examples of Arithmetic Operators
print("********** EXAMPLES OF ARITHMETIC OPERATORS ****************")
# Addition
x = 4895 + 50 
print(x)
# - Subtraction
y = 4895 - 50 
print(y)
# * Multiplication
z = 4895 * 50 
print(z)
# / Division
a = 4895 / 50 
print(a)
# // Division without remainder
b = 4895 // 50 
print(b)
# % Modulus
c = 10 % 3 
print(c)
# ** Exponentiation
d = 2 ** 4 
print(d)

# Examples of comparison operators
a = 15
b = 9
#Greater than
if a > b:
    print('a is greater than b')
    print(a > b)

#Less than
if a < b:
    print('a is less than b')
    print(a < b)
#Greater than or equal to
if a >= b:
    print('a is greater than or equal to b')
    print(a >= b)
#Less than or equal to
if a <= b:
    print('a is greater than or equal to b')
    print(a <= b)
#Equal to
if a == b:
    print('a is equal to b')
    print(a == b)
# Not equal to
if a != b:
    print('a is not equal to b')
    print(a != b)
    
#Examples with Logical Operators
a = True
b = False

#Logical AND 
print(a and b)

#Logical OR 
print(a or b)

#Logical NOT 
print(not a)
print(not b)

#Assignment Operators
# Compound assignment operators

a = 5

# Add and Assign
a += 5 #a = a + 5
print(a) 

# Subtract and Assign
b = 19
b -=5
print(b)

# Multiply and Assign
c = 19
c *= 5
print(c)

# Divide and Assign
d = 19
d /= 5
print(d)

# Modulus and Assign
e = 19
e %= 5
print(e)

# Exponential and Assign
f = 2
f **= 4
print(f)

# Membership assignment operators
cars = ['Jeep', 'Tesla', 'Maserati', 'BMW']
print('Maserati' in cars)

if 'BMW' in cars:
    print('Jeep is in the list')

if 'Bugati' not in cars:
    print('Bugati is not in the list')

# Identity Operators
x = 10
y = 10

#is operator
print(x is y)
print(x is not y)
print(x == y)
print(x < y)
print(x <= y)

#List 
z = [1, 2, 3, 4, 5, 6, 7]
w = [1, 2, 3, 4, 5, 6, 7]

print(z is w)
print(z is not w)
print(z == w) #returns true

# Bitwise operators
"""
Bitwise operators are used to perform operations on individual bits in binary numbers

Bitwise AND ('&'): Performs a bitwise AND operation between the corresponding bits of two integers
Bitwise OR ('|'): Performs a bitwise OR operation between the corresponding bits of two integers
Bitwise XOR ('^'): Performs a bitwise XOR operation 
Bitwise NOT ('~'): Performs a bitwise NOT operation between the corresponding bits of two integers
Bitwise left shift ('<<'): Performs a bitwise left shift operation
Bitwise right shift ('<<'): Performs a bitwise right shift operation

"""


# Example and Assignment
# Bitwise operators example

# Variables
a = 12  # Binary: 1100
b = 7   # Binary: 0111

# Bitwise AND
result_and = a & b
print("Bitwise AND (a & b):", result_and)  # Output: 4 (Binary: 0100)

# Bitwise OR
result_or = a | b
print("Bitwise OR (a | b):", result_or)    # Output: 15 (Binary: 1111)

# Bitwise XOR
result_xor = a ^ b
print("Bitwise XOR (a ^ b):", result_xor)  # Output: 11 (Binary: 1011)

# Bitwise NOT
result_not_a = ~a
print("Bitwise NOT (~a):", result_not_a)   # Output: -13 (Binary: -1101)

result_not_b = ~b
print("Bitwise NOT (~b):", result_not_b)   # Output: -8 (Binary: -1000)

# Bitwise left shift
result_left_shift = a << 2
print("Bitwise left shift (a << 2):", result_left_shift)  # Output: 48 (Binary: 110000)

# Bitwise right shift
result_right_shift = a >> 2
print("Bitwise right shift (a >> 2):", result_right_shift)  # Output: 3 (Binary: 11)

# Example and Assignment
# Create a simple calculator function to calculate (add, subtract, multiply, divide)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    number1 = float(input('Enter the first number: '))
    number2 = float(input('Enter the first number: '))
    operator = (input("Enter the operator (+, -, *, /): "))
    
    if operator == '*':
        result = add(number1, number2)
    elif operator == '-':
        result = subtract(number1, number2)
    elif operator == '*':
        result = multiply(number1, number2)
    elif operator == '/':
        result = divide(number1, number2)
    else:
        print('Invalid operator')
        return
    print("The result is", result)
    
if __name__ == '__main__':
    main()
    
print("Addition: ", add(a, b))
print("Subtraction: ", subtract(a, b))
print("Multiplication: ", multiply(a, b))
print("Division: ", divide(a, b))

# tkinter learn    
#Assignment: Create a simple calculator program with a GUI interface. Make the title of the calculator program with your name eg. "Emma Simple Calculator"
import tkinter as tk

def btn_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))

def btn_clear():
    entry.delete(0, tk.END)

def btn_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Emma's Simple Calculator")
#window.geometry("300x400") to change the overall size of the calculator

# Create the entry widget
entry = tk.Entry(window, width=30, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=30, pady=10)

# Create number buttons
btn_1 = tk.Button(window, text="1", padx=30, pady=15, command=lambda: btn_click(1))
btn_2 = tk.Button(window, text="2", padx=30, pady=15, command=lambda: btn_click(2))
btn_3 = tk.Button(window, text="3", padx=30, pady=15, command=lambda: btn_click(3))
btn_4 = tk.Button(window, text="4", padx=30, pady=15, command=lambda: btn_click(4))
btn_5 = tk.Button(window, text="5", padx=30, pady=15, command=lambda: btn_click(5))
btn_6 = tk.Button(window, text="6", padx=30, pady=15, command=lambda: btn_click(6))
btn_7 = tk.Button(window, text="7", padx=30, pady=15, command=lambda: btn_click(7))
btn_8 = tk.Button(window, text="8", padx=30, pady=15, command=lambda: btn_click(8))
btn_9 = tk.Button(window, text="9", padx=30, pady=15, command=lambda: btn_click(9))
btn_0 = tk.Button(window, text="0", padx=30, pady=15, command=lambda: btn_click(0))


# Create operator buttons
btn_add = tk.Button(window, text="+", padx=30, pady=15, bg="#fff", fg="red", command=lambda: btn_click("+"))
btn_subtract = tk.Button(window, text="-", padx=30, pady=15, bg="#fff", fg="red", command=lambda: btn_click("-"))
btn_multiply = tk.Button(window, text="*", padx=30, pady=15, bg="#fff", fg="red", command=lambda: btn_click("*"))
btn_divide = tk.Button(window, text="/", padx=30, pady=15, bg="#fff", fg="red", command=lambda: btn_click("/"))

# Create other buttons
btn_clear = tk.Button(window, text="C", padx=30, pady=15, bg="#fff", fg="red", command=btn_clear)
btn_equal = tk.Button(window, text="=", padx=30, pady=15, bg="#fff", fg="green", command=btn_equal)

# Place buttons on the grid
btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=1, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_7.grid(row=3, column=0)
btn_8.grid(row=3, column=1)
btn_9.grid(row=3, column=2)
btn_0.grid(row=4, column=0)
btn_add.grid(row=1, column=3)
btn_subtract.grid(row=2, column=3)
btn_multiply.grid(row=3, column=3)
btn_divide.grid(row=4, column=3)
btn_clear.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)

# Start the main event loop
window.mainloop()

    