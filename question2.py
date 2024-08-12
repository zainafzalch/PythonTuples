# 2. Python Data Structure Challenges in Real-World Scenarios

# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

try:
    year = input("Enter year of book: ")
    author = input("Enter author of book: ")
    if (year, author) not in library:
        library.append((year,author))
    else:
        print("Book already exists!")
except ValueError as e:
    print(e)
finally:
    print(library)