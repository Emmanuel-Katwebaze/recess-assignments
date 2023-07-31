# Inheritance

# Parent class
from tkinter import messagebox
import tkinter as tk
from abc import ABC, abstractmethod
import math


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

# Child class inheriting from Vehicle


class Car(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} is driving.")

# Child class inheriting from Vehicle


class Motorcycle(Vehicle):
    def __init__(self, brand, year, speed):
        super().__init__(brand, year)
        self.speed = speed

    def ride(self):
        print(f"{self.brand} motorcycle is riding at {self.speed} mph.")


# Creating objects of the classes
car = Car("Toyota", 2020, "Red")
motorcycle = Motorcycle("Harley-Davidson", 2019, 60)

# Accessing inherited methods
car.start()
car.drive()
car.stop()

motorcycle.start()
motorcycle.ride()
motorcycle.stop()

# Accessing inherited attributes
print(f"Car: {car.brand} {car.year}, Color: {car.color}")
print(
    f"Motorcycle: {motorcycle.brand} {motorcycle.year}, Speed: {motorcycle.speed}")

print("**********************************************************")


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking...")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing...")


# Create Animal objects
animal = Animal("Generic Animal")
dog = Dog("Spot")
cat = Cat("Fluffy")

# Invoke call eat method
animal.eat()
dog.eat()
dog.bark()
cat.eat()
cat.meow()

print("************************************************************")
# Example2 Demonstrating inheritance


class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand} color: {self.color}")

    def move(self):
        print("Moving the vehicle...")


class Car(Vehicle):
    def __init__(self, brand, color, num_wheels):
        super().__init__(brand, color)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print("Number of Wheels:", self.num_wheels)

    def honk(self):
        print("Honking the horn...")


# Create a car object
my_car = Car("Toyota", "Red", 4)

# Access and modify the car attributes
print("Brand:", my_car.brand)  # Output: Brand: Toyota

# Invoke the car methods
my_car.display_info()
my_car.move()
my_car.honk()

print("*************************** EXERCISE 1  **************************************")
# Exercise1
# Demonstrate using inheritance to calculate area and perimeter of circle and rectangular area
# respectively (base class. Shape)


# Base class

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


circle = Circle(10)
rectangle = Rectangle(5, 9)

circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()

rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()

print(f"Circle - Area: {circle_area:.2f}, Perimeter: {circle_perimeter:.2f}")
print(f"Rectangle - Area: {rectangle_area}, Perimeter: {rectangle_perimeter}")


# Example 3
print("*************************** Example 3 **************************************")

# Multiple Inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")


class Flyable:
    def fly(self):
        print(f"{self.name} is flying...")


class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def display_info(self):
        print(f"Species: {self.species}")
        print(f"Name : {self.name}")


# Create a bird object
my_bird = Bird("Eagle", "predator")

# Invoke the Bird methods
my_bird.eat()
my_bird.fly()
my_bird.display_info()

# Method overridding

print("************************ Method overriding *******************************")


class Animal:
    def make_sound(self):
        print("Animal is making a sound!")


class Dog(Animal):
    def make_sound(self):
        print("Dog is barking!")


class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing!")


def make_animal_sound(animal):
    animal.make_sound()


# Create objects
animal = Animal()
dog = Dog()
cat = Cat()

# Calling make_animal_sound function
make_animal_sound(animal)
make_animal_sound(dog)
make_animal_sound(cat)

# Calling make_sound function
dog.make_sound()
cat.make_sound()
animal.make_sound()

# Polymorphism allows you to write code that can work with different objects

# Method Overriding occurs whena derived class, sub class, (child class), provides it's own
# implementation of a method that is already defined in its base class
# Method Overloading allows a class to have multiple methods with the same name but different parameters

# Example4
print("************************ Example 4 *******************************")


class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

    def calculate_circumference(self):
        return 2 * 3.14 * self.radius


# Create shape objects
rectangle = Rectangle(5, 5)
circle = Circle(5)

# Calculate and display area
print("Area of rectangle", rectangle.calculate_area())
print("Area of circle", circle.calculate_area())


# Overloading functions
class Calculate:
    def add(x, y):
        return x + y

    def add(x, y, z):
        return x + y + z


obj1 = Calculate()
# obj1.add(1, 2)
# obj1.add(2, 3, 4)
# Python calls the last defined function


# Abstraction
# Allow you to focus on essential features and hide them from unecessary details

print("************************ Example 5 *******************************")
# Example5: Demonstrate abstration


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Starting the car...")

    def stop(self):
        print("Stopping the car...")


class Truck(Vehicle):
    def start(self):
        print("Starting the truck...")

    def stop(self):
        print("Stopping the truck...")


# Create the objects
car = Car()
truck = Truck()

# Start the vehicle
car.start()
truck.start()

print("************************ Personal Example *******************************")

# Abstract base class


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Concrete class inheriting from Shape


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# Creating objects of the classes
rectangle = Rectangle(4, 6)

# Trying to create an object of the abstract base class
# shape = Shape()  # This will raise a TypeError

# Accessing the concrete class's method
area = rectangle.calculate_area()
print(f"Rectangle area: {area}")

print("************************ Exercise 2 *******************************")
# Exercise 2: Demonstrate abstraction using calculating area of a
# circle and rectangle


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

    def calculate_circumference(self):
        return 2 * 3.14 * self.radius


# Create shape objects
rectangle = Rectangle(5, 5)
circle = Circle(5)

# Calculate and display area
print("Area of rectangle", rectangle.calculate_area())
print("Area of circle", circle.calculate_area())

# Assignment
# Create a receipt printing program with GUI interface, a more advanced detail
# earns you more marks


class ReceiptPrinter(tk.Frame):
    def __init__(self, master):
        self.master = master
        master.title("Emma temple, inc.")

        self.items = []  # List to store added items

        self.item_name_label = tk.Label(master, text="Item:")
        self.item_name_label.pack()

        self.item_name = tk.Entry(master)
        self.item_name.pack()

        self.item_price_label = tk.Label(master, text="Price:")
        self.item_price_label.pack()

        self.item_price = tk.Entry(master)
        self.item_price.pack()

        self.submit_button = tk.Button(
            master, text="Add Item", command=self.add_item)
        self.submit_button.pack()

        self.print_button = tk.Button(
            master, text="Print Receipt", command=self.print_receipt)
        self.print_button.pack()

        self.receipt_text = tk.Text(master, height=20, width=50)
        self.receipt_text.pack()

    def add_item(self):
        item = self.item_name.get()
        price = self.item_price.get()

        if item and price:
            try:
                price = float(price)  # Convert price to float
            except ValueError:
                messagebox.showerror(
                    "Error", "Invalid price format. Please enter a number.")
                return

            self.items.append((item, price))  # Add item to the list
            self.receipt_text.insert(tk.END, f"Item: {item}, Price: {price}\n")
            self.item_name.delete(0, tk.END)
            self.item_price.delete(0, tk.END)

        else:
            messagebox.showerror("Error", "Please enter both item and price.")

    def print_receipt(self):
        company_name = "Emma temple, inc."
        company_address = "Kireka B."
        company_city = "K'LA"

        self.receipt_text.delete(1.0, tk.END)  # Clear the receipt text

        self.receipt_text.insert(tk.END, "*" * 50 + "\n")
        self.receipt_text.insert(
            tk.END, "\t\t{}\n".format(company_name.title()))
        self.receipt_text.insert(tk.END, "\t\t{}\n".format(company_address))
        self.receipt_text.insert(tk.END, "\t\t{}\n".format(company_city))
        self.receipt_text.insert(tk.END, "=" * 50 + "\n")
        self.receipt_text.insert(tk.END, "\tProduct Name\tProduct Price\n")

        total = 0.0
        for item, price in self.items:
            self.receipt_text.insert(
                tk.END, "\t{}\t\t${}\n".format(item.title(), price))
            total += float(price)

        self.receipt_text.insert(tk.END, "=" * 50 + "\n")
        self.receipt_text.insert(tk.END, "\t\t\tTotal\n")
        self.receipt_text.insert(tk.END, "\t\t\t${}\n".format(total))
        self.receipt_text.insert(tk.END, "=" * 50 + "\n")
        self.receipt_text.insert(
            tk.END, "\n\tThanks for shopping with us today!\n")
        self.receipt_text.insert(tk.END, "*" * 50 + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = ReceiptPrinter(root)
    root.mainloop()


# RESEARCH MADE FROM PYTHON TEXTBOOK
# create a product and price for three items
p1_name, p1_price = "Books", 49.95
p2_name, p2_price = "Computer", 579.99
p3_name, p3_price = "Monitor", 124.89

# create a company name and information
company_name = "coding temple, inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"

# declare ending message
message = "Thanks for shopping with us today!"

# create a top border
print("*" * 50)

# print company information first, using format
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))

# print a line between sections
print("=" * 50)

# print out header for section of items
print("\tProduct Name\tProduct Price")

# create a print statement for each product
print("\t{}\t\t${}".format(p1_name.title(), p1_price))
print("\t{}\t\t${}".format(p2_name.title(), p2_price))
print("\t{}\t\t${}".format(p3_name.title(), p3_price))

# print a line between sections
print('=' * 50)

# print out header for section of total
print("\t\t\tTotal")

# calculate total price and print out
total = p1_price + p2_price + p3_price
print("\t\t\t${}".format(total))

# print a line between sections
print("=" * 50)

# output thank you message
print("\n\t{}\n".format(message))

# create a bottom border
print("*" * 50)
