# Object-Orientated Programming(OOP)
# Key concepts in OOP are

"""
1. Class
2. Objects
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction

# Class
- A class is a blueprint for creating objects.
"""
# Example1: Car


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")


my_car = Car("Toyata", "Corolla", 2022)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()

# Example 2: BankAccount


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds to withdraw")

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


# Create Bank Account object
my_account = BankAccount("1234567", 1000)

# Perform operations on the Bank Account object
my_account.display_balance()
my_account.deposit(500)
my_account.withdraw(200)
my_account.display_balance()


# Example3: Rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Create a Rectangle
my_rectangle = Rectangle(15, 4)
print(my_rectangle.length)
print(my_rectangle.width)

# Calculate and display the are of the rectangle and perimeter
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())

# Example4: Student


class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course

    def display_details(self):
        print("Name: ", self.name)
        print("Year: ", self.year)
        print("Course: ", self.course)


student = Student("Emma", "Year 2", "BSSE")

# Display the Student details
student.display_details()


class Animal:
    def __init__(self, name, color, no_of_legs, sound):
        self.name = name
        self.color = color
        self.no_of_legs = no_of_legs
        self.sound = sound

    def show_details(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Number of Legs:", self.no_of_legs)
        print("Sound:", self.sound)

    def makeSound(self):
        print(f"The {self.name} is {self.sound}")


animal1 = Animal("Dog", "brown", 4, "barking")
animal1.show_details()
animal1.makeSound()

# Object


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)
        print("I am,", self.age, "years old")

# Create a Person object


my_person1 = Person("Emma", 21)
my_person2 = Person("Zoe", 20)

# Accessing the Person object attributes
print(my_person1.name)
print(my_person1.age)
print(my_person2.name)
print(my_person2.age)

# Invoke our object method
my_person1.greet()
my_person2.greet()

# Exercise
# Calculate the area and circumference of a circle


class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return Circle.PI * self.radius**2

    def calculate_circumference(self):
        return 2 * Circle.PI * self.radius


circle1 = Circle(10)
print("The area of a circle of radius",
      circle1.radius, "is", circle1.calculate_area())
print("The circumference of a circle of radius",
      circle1.radius, "is", circle1.calculate_circumference())

# Exercise 2
# Calculate and display employee bonuses(15%) of salary (employee1: 150000, employee2: 230000)


class Employee:
    bonus = 0.15

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_bonus(self):
        print("For", self.name, "the bonus is", self.salary * Employee.bonus)


employee1 = Employee("John", 150000)
employee1.get_bonus()
employee2 = Employee("Jahn", 230000)
employee2.get_bonus()

# Encapsulation
# Main goals of encapsulation are:
"""
1. To hide the implementation details of an object
2. To protect the object from changes
3. To protect the object from external changes
4. Code organization and modularity

"""
# Example with a bank account


class BankAccount:
    def __init__(self, account_number, balance):
        # Encapsulates the account number attribute
        self._account_number = account_number
        self._balance = balance  # Encapsulates the balance attribute

    def deposit(self, amount):
        self._balance += amount  # Encapsulates the deposit

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount  # Encapsulates the withdra
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance


# Create a Bank Object
my_account = BankAccount("123456789", 1000)

# Access the Bank Object and modify encapsulated attributes indirectly
print(my_account._account_number)
print(my_account._balance)
my_account.deposit(500)
print(my_account._balance)
my_account.withdraw(100)
print(my_account._balance)

# Exercise 2: Convert temperature(37) from Celsius to Fahrenheit


class Temperature:
    def __init__(self, temperature):
        self._temperature = temperature

    def convert(self):
        fahrenheit = (self._temperature * 9 / 5) + 32
        print(f"{self._temperature} degrees Celsius to Fahrenheit is {fahrenheit}")


temp1 = Temperature(37)
temp1.convert()

# Encapsulation demonstrating the goals of encapsulation


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age

    def __str__(self):
        return f"Person: {self._name}, Age: {self._age}"


# Creating an instance of Person
person = Person("John", 25)

# Goal 1: Hiding implementation details
print(person.get_name())  # Accessing name via getter method

# Goal 2: Protecting the object from changes
person.set_age(30)  # Updating age using setter method
print(person.get_age())  # Accessing age via getter method

# Goal 3: Protecting the object from external changes
# print(person._name)  # This will not raise an AttributeError but is not recommended

# Goal 4: Code organization and modularity
print(person)  # Using the __str__() method for string representation

# Assignment1: Show encapsulation with employee information to give a pay incrementation
# (Salary with employee information to new_salary ) eg from 850000 to 1000000


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def give_raise(self, increment_amount):
        if increment_amount > 0:
            self._salary += increment_amount
            print(f"{self._name}'s salary has been increased by {increment_amount}.")
        else:
            print("Invalid increment amount. Salary remains unchanged.")


employee1 = Employee("Emmanuel K", 50000)
employee2 = Employee("Shanice K", 60000)

print(f"{employee1.get_name()} earns {employee1.get_salary()}")

print(f"{employee2.get_name()} earns {employee2.get_salary()}")

employee2.give_raise(-2000)

print(f"{employee1.get_name()} now earns {employee1.get_salary()}")

print(f"{employee2.get_name()} still earns {employee2.get_salary()}")
