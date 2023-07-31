# DAY 7
# Remaining concepts in Advanced Python Topics

# Context Manager
# Multithreading and Multiprocessing

# Context Manager - is an object that defines a temporary context for a block
# of code

# Example1: Demonstrate a context manager to open a file and returns
# a context manager instance

# def open_file(filename):
#     #Open a file and return a context manager instance
#     file = open(filename, "r")

#     def __enter__():
#         return file

#     def __exit__(self, exc_type, exc_value,exc_tb):
#         file.close()

#         return __enter__, __exit__

# with open_file("my_file.txt") as f:
#     contents = f.read()

# Example 2: Demonstrate a context manager using a time series
import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f"The time for this execution {execution_time} seconds elapsed")


# With Example Usage
with Timer():
    # measure the execution time
    time.sleep(2)

# Mutlithreading and multiprocessing
# techniques that can be used to improve performance of a Python program

# Multithreading is a technique where multiple threads are created within a single process
# Multiprocessing is a technique where multiple threads are created.

# Example of multithreading
import threading

def task(name):
    print(f'Running task {name}')


# Create multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=task, args={f"Thread {i}", })
    threads.append(t)
    t.start()

# Wait for all threads to finish before it joins

for t in threads:
    t.join() 
    

# Example4: Demonstrate use of multiprocessing

import multiprocessing

def process_task(name):
    print(f"Processing task {name}")

if __name__ == '__main__':
    # Create a pool of processes
    pool = multiprocessing.Pool(processes=5)

    # Submit multiple tasks to the pool
    for i in range(6):
        pool.apply_async(process_task, args=(f"Process {i}",))

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()



# Example5: Demonstrate use of multithreading and multiprocessing
import threading
import multiprocessing

def task(name):
    print(f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")
    

# Create multiple threads
threads = []
for i in range(4):
    t = threading.Thread(target=task, args=(f"Thread {i}", ))
    threads.append(t)
    t.start()


# Wait for all threads to finish
for t in threads:
    t.join()

# Assignment A7:
# 1a) Show a context manager for file handling that automatically opens and closes a file.
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        # Open the file when entering the context
        self.file = open(self.filename, self.mode)  
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()  # Close the file when exiting the context

# Example usage:
with FileHandler('file.txt', 'w') as file:  # Create an instance of FileHandler and assign it to 'file'
    file.write('Hello, Emma!')  # Write 'Hello, world!' to the file
    
# b) Shows a context manager for managing a database connection.    

import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        try:
            self.connection = sqlite3.connect(self.db_name) # Establish a connection to the database
            return self.connection
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print("An error occurred during the execution:", exc_value)
        try:
            self.connection.close() # Close the database connection when exiting the context
        except sqlite3.Error as e:
            print("Error closing the database connection:", e)

# Example usage:
with DatabaseConnection('mydb.db') as conn:  # Create an instance of DatabaseConnection and assign it to 'conn'
    if conn is not None:
        try:
            cursor = conn.cursor() # Create a cursor object to execute SQL statements
             # Add three data items to the 'users' table
            query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, email TEXT, phone TEXT)"
            with conn:
                conn.execute(query)
            users = [
                ('Emma', 'Kats', 'emma.kats@example.com'),
                ('Maria', 'Musiimenta', 'maria.musiimenta@example.com'),
                ('Joseph', 'Johnson', 'joseph.johnson@example.com')
            ]
            cursor.executemany('INSERT INTO users (first_name, last_name, email) VALUES (?, ?, ?)', users)
            conn.commit()
            cursor.execute("SELECT * FROM users") # Execute the SQL query
            result = cursor.fetchall() # Fetch all the results from the query
            print(result)  # Print the results
        except sqlite3.Error as e:
            print("Error executing SQL query:", e)
            

    
    
# c) Show a multithreading and multiprocessing  that 
# allows us to run the function for different amounts of time.
import time
import threading
import multiprocessing

def run_function(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        pass
    print(f"Finished running for {duration} seconds.")

if __name__ == '__main__':
    # Multithreading example
    thread1 = threading.Thread(target=run_function, args=(3,))
    thread2 = threading.Thread(target=run_function, args=(5,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # Multiprocessing example
    process1 = multiprocessing.Process(target=run_function, args=(3,))
    process2 = multiprocessing.Process(target=run_function, args=(5,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()



