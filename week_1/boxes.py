"""
Title: Calculator for the Number of Needed Boxes
Author: Clinton Jake Cai
Description: A program used to practice invoking built-in and standard library functions
"""
# Imports the math library
import math

# Gets the number of the manufactured items
number_of_items = int(input("\nPlease type the number of items: "))

# Gets the number of items that the user will pack per box
items_per_box = int(input("Please type how many items per box: "))

# Computes the total box needed by doing a division and rounding it up
total_needed_box = math.ceil(number_of_items / items_per_box)

# Display the result
print(f"With the given number of {number_of_items} items, {total_needed_box} boxes is/are needed to fit for {items_per_box} items per box.")