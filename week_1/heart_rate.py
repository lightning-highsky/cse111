"""
Title: Heart Rate Exercise Calculator
Author: Clinton Jake Cai
Description:
    When you physically exercise to strengthen your heart, you
    should maintain your heart rate within a range for at least 20
    minutes. To find that range, subtract your age from 220. This
    difference is your maximum heart rate per minute. Your heart
    simply will not beat faster than this maximum (220 - age).
    When exercising to strengthen your heart, you should keep your
    heart rate between 65% and 85% of your heart’s maximum rate.
"""

# Gets the age of the user
age = int(input("Please enter your age: "))

# Subtracts the age from 220 to get the maximum heart rate per minute
max_heart_rate_per_min = 220 - age

# Calculates the lowest and highest heart rate possible of the user
lowest_heart_rate_needed = int(max_heart_rate_per_min * 0.65)
highest_heart_rate_needed = int(max_heart_rate_per_min * 0.85)

# Displays the result
print("To physically strengthen your heart through exercise, you need to maintain your heart rate per minute "
      f"between {lowest_heart_rate_needed} and {highest_heart_rate_needed} within 20 minutes.")