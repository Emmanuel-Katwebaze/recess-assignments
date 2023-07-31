# DAY 2 MODULE 2

"""
#Control Flow
Conditional Statements (if-elif-else)

if gen_gender_sex:
    print('Male')
else: 
    print('Female')
    
"""
"""
if condition1:
    print('True') # code block is executed if condition is True
elif condition2:
    print('True') #code block is only executed if condition2 is True
else:
    print('False') #code block is only executed if all conditions are False
"""

#Example 1

#age <18, Print "You are underage"
#age >= 18 and age <=65 "You're an adult"
#print "You are a senior citizen"

age = 21
if age < 18:
    print("You are underage")
elif age >=18 and age <= 65:
    print("You are an adult")
else:
    print("You are a senior citizen")
    

#Loops
#Include for and while loops
# for item in collection

cars = ['Tesla', 'Jeep', 'Ford', 'Toyota', "BMW"]

for car in cars:
    print(car)
    
#fruits
fruits = ['mangoes', 'guavas', 'oranges', 'pineapples']
for fruit in fruits:
    print("I eat " + fruit) 
    
#while loop 
#Example
 
x = 0
while x < 5:
    print(x)
    x+=1
    
fruits = ['mangoes', 'guavas', 'oranges', 'pineapples']
fruit_count = 0
while fruit_count < len(fruits):
    print("I eat " + fruits[fruit_count]) 
    fruit_count +=1

numbers = [0, 1, 2, 3, 4, 5, 6]
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:
        print(str(numbers[index]) + " is even")
    else:
        print(str(numbers[index]) + " is odd")
    index+=1
 
print("*********************************")
for number in range(1,10):
    if number == 5:
        break
    print(number)   

print("*********************************")
for number in range(1,10):
    if number == 5:
        continue
    print(number)
    
print("***************  Prints only odd numbers ******************")   
for number1 in range(1,10):
    if number1 % 2 == 0:
        continue
    else:
        print(str(number1) + " is odd")
    
print("**************** Prints only 0 *****************")   
for number2 in range(0,10):
    if number2 % 2 == 0:
        print(str(number2) + " is even")
    else:
        break
    
"""
try block

except:

finally:
"""

print("*********************************")
try:
    x = 10/0
except ZeroDivisionError:
    print('Error: Division by Zero') #cannot divide by zero
finally:
    print('This is always executed') #Complete execution
    
print("*********************************")   
def access_array_element(arr, index):
    try:
        value = arr[index]
        print("Value at index", index, "is:", value)

    except IndexError:
        print("Error: Index out of bounds.")

    finally:
        print("Array access operation complete.")


my_array = [1, 2, 3, 4, 5]

# Example 1: Valid index
access_array_element(my_array, 2)

# Example 2: Invalid index
access_array_element(my_array, 10)

print("*********************************") 
class UnderAgeException(Exception):
    pass


def check_age(age):
    if age < 18:
        raise UnderAgeException("You must be 18 or older to access this content.")


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
    
print("*********************************")
# Example5
emotions = {
    'happy' : "I'm glad to hear you're happy",
    'sad' : "I'm sorry to hear that you're feeling sad",
    "angry": "take a deep breath and try to stay alive",
    "fearful": "I understand that fear can be challenging",
    'disgusted': "That's unfortunate to feel disgusted at this time"
}

#prompt the user ro enter their emotion
user_emotion = input("How are you feeling today? ")
user_emotion = user_emotion.lower()
if user_emotion in emotions:
    print(emotions[user_emotion])
else:
    print("I'm sorry, I don't understand that emotion")

# EXERCISE
# Write a program to ask students about their mental health

emotions = {
    'happy': "I'm glad to hear you're happy",
    'sad': "I'm sorry to hear that you're feeling sad",
    'angry': "Take a deep breath and try to stay calm",
    'fearful': "I understand that fear can be challenging",
    'disgusted': "That's unfortunate to feel disgusted at this time"
}

def get_user_input():
    while True:
        print("How are you feeling today?")
        print("1. Happy")
        print("2. Sad")
        print("3. Angry")
        print("4. Fearful")
        print("5. Disgusted")
        choice = input("Enter your choice (1-5): ")
        if choice.isdigit() and 1 <= int(choice) <= 5:
            return int(choice)
        else:
            print("Invalid input. Please enter a number between 1 and 5.\n")

def main():
    choice = get_user_input()
    emotion = list(emotions.keys())[choice - 1]
    message = emotions[emotion]
    print(message)
    print("     *****")
    print("   **     **")
    print(" **         **")
    print("**    o o    **")
    print("**     ^     **")
    print(" **   '-'   **")
    print("   **     **")
    print("     *****")

# Run the main program
main()

# EXERCISE
# Write a program to ask students about their mental health
# Prompt student on the scale of one to 10 to rate their mental health

mental_health = input("Rate your mental health from one to 10 \{ 1 to 10 \}" )
mental_health = int(mental_health)
if mental_health in range(1,3):
    print("Please hang on... everything will be alright")
elif mental_health in range(4,7):
    print("Take a deep breath and look forward to tomorrow")
elif mental_health in range(8, 10):
    print("That's great, remember you are a very strong human being")
else:
    print("Please enter a value within the range")
print("Thank you for taking this survey")
print("     *****")
print("   **     **")
print(" **         **")
print("**    o o    **")
print("**     ^     **")
print(" **   '-'   **")
print("   **     **")
print("     *****")

    

