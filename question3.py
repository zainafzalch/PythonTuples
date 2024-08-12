# 3. Mastering Tuple Packing and Unpacking in Python

# Objective: The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python.

# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

# Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

# Sample Order Data:

# orders = [
#     ("Alice", "Laptop", 1),
#     ("Bob", "Camera", 2),
#     # More orders...
# ]

# - Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2)
]

def print_order(orders):
    for name, product, quantity in orders:
        print(f"{name} ordered {quantity} {product}.")

print_order(orders)