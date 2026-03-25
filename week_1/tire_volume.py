"""
Title: Tire Volume Calculator
Author: Clinton Jake Cai
Description: A program that computes for a tire's volume using soft code, and logging the data to a file.
Enhancement: I made the program to do a while loop depending on the user's need, allowing them to do multiple calculations in one program run. I also made it to be user-friendly through using the user's name.
"""

# Declaration of Libraries and Variables
import math
from datetime import datetime

user_name = ""
width = 0
aspect_ratio = 0
diameter = 0
volume = 0
date = ""
user_need = "yes"

# Welcome Message
user_name = input("\nHello there! This is a Tire Volume Calculator. But first, what is you name? ").title()
print(f"\nNice to meet you, {user_name}! This program functions using the US standard tire information, represented with three numbers like this:"
      " 205/60R15. The first number is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits.")

# Uses while loop depending on the user's need
while user_need == "yes":
    # Asking for the tire's width in mm
    width = int(input("\nPlease indicate the tire's width in mm (e.g. 260): "))
    
    # Asking for the aspect ratio
    aspect_ratio = int(input("Please indicate the tire's aspect ratio (e.g. 60): "))

    # Asking for the diameter of the wheel in inches
    diameter = int(input("Please indicate the wheel's diameter in inches (e.g. 15): "))

    # Calculate the tire's volume
    volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

    # Displays the tire's volume (rounded to two decimal places)
    print(f"\nThe approximate volume is: {volume:.2f}")

    # Logs the information in a text file: current date (without the time), tire's width, aspect ratio, diameter of the wheel, and the volume of the tire (rounded to two decimal places)
    # Get the current date using datetime module
    date = datetime.now()
    
    # Stores the information using the open function
    with open("volumes.txt", "a") as volumes_file:
        print(f"{date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=volumes_file)

    # Confirms if the user need's another computation
    user_need = input(f"\n{user_name}, would you like to continue compute again? Type YES or NO ").lower()
    
    if user_need == "yes":
        continue
    elif user_need == "no":
        print("Thanks for having us!")
    else:
        print("Sorry, I didn't get that. The program will stop. Thanks for having us!")