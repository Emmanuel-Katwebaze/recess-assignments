# Python Exception Handling

"""Exception handling allows you to gracefully handle and 
recover from runtime errors in your Python programs
=> try block - code that will  throw an exception
=> except block - code that will handle the exception
=> finally block - code that executes irrespective of whether the error occurs
    or not

try:
    # code that will throw an exception
except:
    # code that handles the error
finally:  
    # run regardless of outcome

"""
import os
import tempfile
print("******** Exception handling using a single except block **********")


def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
        # You can choose to handle the exception in different ways, like returning a default value or raising a new exception.


# Calling the method that throws an exception
num1 = 10
num2 = 0

try:
    result = divide_numbers(num1, num2)
    print("Result:", result)
except ZeroDivisionError:
    print("Error occurred during division.")
finally:
    print("Execution finished.")


def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except TypeError:
        print("Error: Invalid types for division!")
    except Exception as e:
        print("An unexpected error occurred:", str(e))


print("******** Exception handling using multiple except blocks **********")

num1 = 10
num2 = 0
num3 = '5'


def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")


try:
    result = divide_numbers(num1, num2)  # Here the ZeroDivisionError is raised
    print("Result:", result)
except ZeroDivisionError:
    print("Error occurred due to division by zero.")
except TypeError:
    print("Error occurred due to invalid types.")
except Exception as e:
    print("An unexpected error occurred:", str(e))


try:
    result = divide_numbers(num1, num3)  # Here the TypeError is raised
    print("Result:", result)
except ZeroDivisionError:
    print("Error occurred due to division by zero.")
except TypeError:
    print("Error occurred due to invalid types.")
except Exception as e:
    print("An unexpected error occurred:", str(e))


print("******** Custom Exceptions **********")
# Here you must inherit from the Exception base class


class InvalidAgeException(Exception):
    def __init__(self, message="You must be 18 or older to access this content."):
        self.message = message
        super().__init__(self.message)


def validate_age(age):
    if not isinstance(age, int) or age < 18:
        raise InvalidAgeException()  # Explicitly raise an exception


# Example usage
try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Valid age!")
except InvalidAgeException as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a valid age.")

print("******** Custom Exceptions Example 2 **********")


class UnderAgeException(Exception):
    pass


def check_age(age):
    if age < 18:
        raise UnderAgeException(
            "You must be 18 or older to access this content.")


try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
    print("Access granted. You can view the content.")

except ValueError:
    print("Invalid input. Please enter a valid age.")

except UnderAgeException as e:
    print("Error:", str(e))

finally:
    print("Program execution complete.")

# Creating a file and writing to it
file_name = "file.txt"
file = open(file_name, "w")  # Open the file in write mode

file.write("Good morning\n")
file.write("How are you?\n")
file.write("It is a brand new day\n")

file.close()  # Close the file

# Reading from a file
file = open(file_name, "r")  # Open the file in read mode

# Read the entire contents of the file
contents = file.read()
print("File Contents:")
print(contents)

file.close()  # Close the file

# Reading line by line
file = open(file_name, "r")  # Open the file in read mode

print("\nFile Contents (Line by Line):")
for line in file:
    print(line.strip())  # Strip newline character from each line

file.close()  # Close the file


print("******** Manipulating files using the with statement **********")

file_name = "file.txt"

# Writing to a file using 'with' statement
with open(file_name, "w") as file:
    file.write("Good morning\n")
    file.write("How are you?\n")
    file.write("It is a brand new day\n")

# Reading from a file using 'with' statement
with open(file_name, "r") as file:
    contents = file.read()
    print("\nFile Contents:")
    print(contents)

# Reading line by line using 'with' statement
with open(file_name, "r") as file:
    print("\nFile Contents (Line by Line):")
    for line in file:
        print(line.strip())  # Strip newline character from each line


print("******** Appending to a file **********")

# Appending to a file
file_name = "file.txt"

# Appending to a file using 'with' statement
with open(file_name, "a") as file:
    file.write("This line will be appended.\n")
    file.write("Appending more text to the file.\n")

# Reading the file after appending
with open(file_name, "r") as file:
    contents = file.read()
    print("File Contents:")
    print(contents)


print("****** Reading and manipulating file contents using rstrip() and lstrip() **********")

# Reading and manipulating file contents using rstrip() and lstrip()
# lstrip() - The lstrip() method removes leading characters from the left end of a string
# rstrip() - The rstrip() method removes trailing characters from the right end of a string.

file_name = "file.txt"

# Writing some content to the file
with open(file_name, "w") as file:
    file.write("   This line has leading and trailing spaces.   \n")
    file.write("This line has a trailing newline character.\n")
    file.write("   This line has leading and trailing tabs.   \t\t\n")

# Reading the file and manipulating the content
with open(file_name, "r") as file:
    # Reads all lines from the file and returns them as a list.
    contents = file.readlines()

    # Removing leading and trailing spaces and tabs
    contents_stripped = [line.strip() for line in contents]

    # Removing only leading spaces and tabs
    contents_lstripped = [line.lstrip() for line in contents]

    # Removing only trailing spaces and tabs
    contents_rstripped = [line.rstrip() for line in contents]


# Note
# [line.rstrip() for line in contents]
# is a list comprehension in Python that processes each line in the
# contents sequence and applies the rstrip()
#  print(line, end="") the print statement that prints the current line without adding a
# newline character (end="" is used to specify an empty string as the end character


# Printing the original and manipulated contents
print("Original Contents:")
for line in contents:
    print(line, end="")

print("\nContents after strip():")
for line in contents_stripped:
    print(line)

print("\nContents after lstrip():")
for line in contents_lstripped:
    print(line)

print("\nContents after rstrip():")
for line in contents_rstripped:
    print(line)

print("****** Accessing a file using a path **********")


# Accessing a file using a path
file_path = "C:\\Users\\dell\\Desktop\\Recess\\DAY 5\\file.txt"

# Check if the file exists
if os.path.exists(file_path):
    # Opening the file in read mode
    with open(file_path, "r") as file:
        contents = file.read()
        print("File Contents:")
        print(contents)
else:
    print(f"The file at path '{file_path}' does not exist.")


# Open a file in 'x' mode for exclusive creation
try:
    with open('new_file.txt', 'x') as file:
        file.write('This is a new file.')
        print('File created successfully.')
except FileExistsError:
    print('File already exists. Cannot create a new file.')


print("****** Using tempfile concept **********")

# Create a temporary file
with tempfile.NamedTemporaryFile() as temp_file:
    # Write some data to the file
    temp_file.write(b'Hello, World!')

    # Seek back to the beginning of the file
    temp_file.seek(0)

    # Read and print the file content
    content = temp_file.read()
    print(content.decode())

# The temporary file is automatically deleted at the end of the 'with' block


"""
Note ONE: 
1. t mode (text mode): This is the default mode if no mode is specified.
2. b mode (binary mode): In binary mode, data is read or written as a sequence of bytes.

# Reading from a text file (default mode is 't')
with open('text_file.txt', 'rt') as text_file:
    contents = text_file.read()
    print(contents)

# Reading from a binary file
with open('binary_file.bin', 'rb') as binary_file:
    data = binary_file.read()
    print(data)


Note TWO: Different os module methods related to file handling

1. os.path.exists(path): Checks whether a file or directory exists at the specified path.

2. os.path.isfile(path): Checks whether the specified path corresponds to a file.

3. os.path.isdir(path): Checks whether the specified path corresponds to a directory.

4. os.path.basename(path): Returns the base name of the file or directory from the given path.

5. os.path.dirname(path): Returns the directory name from the given path.

6. os.path.join(path1, path2, ...): Joins multiple path components intelligently and returns a new path.

7. os.listdir(directory): Returns a list of files and directories in the specified directory.

8. os.mkdir(path): Creates a new directory at the specified path.

9. os.makedirs(path): Creates a new directory and any necessary intermediate directories at the specified path.

10. os.remove(path): Removes (deletes) a file at the specified path.

11. os.rmdir(path): Removes an empty directory at the specified path.

12. os.removedirs(path): Removes a directory and any empty intermediate directories at the specified path.

13. os.rename(src, dst): Renames a file or directory from the source path to the destination path.

14. os.getcwd(): Returns the current working directory.

15. os.chdir(directory): Changes the current working directory to the specified directory.

16. os.stat(path): Returns information about a file or directory at the specified path."""
