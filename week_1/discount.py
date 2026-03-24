"""
Program: Discount Calculator for Tuesday & Wednesday
Author: Clinton Jake Cai
Description: Calculates the discount of a user depending to the day.
"""
# Declare variables and library
from datetime import datetime

quantity = None
price = 0
initial_subtotal = 0
subtotal = 0
target_subtotal = 50
discount_percent = 0
discount_amount = 0
needed_subtotal = 0
sales_tax_percent = 0.06
sales_tax_amount = 0
amount_due = 0

# Gets the current day information for the selection statements
today = datetime.now()
dow = today.weekday()

quantity = int(input("How many items for this set of products? (Type 0 once done) "))
# Asks the user for the quantity and the price in a loop
while quantity != 0:
    price = float(input("What is the price per item: "))
    initial_subtotal += quantity * price
    quantity = int(input("How many items for another set of products? (Type 0 if none) "))

# Computes the discount on the subtotal if applicable
if dow == 1 or dow == 2:
    if initial_subtotal >= target_subtotal:
        discount_percent = 0.1
        discount_amount = initial_subtotal * discount_percent
        initial_subtotal -= discount_amount

    # Computes the needed additional subtotal to avail the discount if applicable
    else:
        needed_subtotal = target_subtotal - initial_subtotal

        # Prints an information about the needed additional subtotal
        print(f"To avail the discount this day, you need an additional ${needed_subtotal}.")

# Computes the sales tax amount based on the subtotal

sales_tax_amount = initial_subtotal * sales_tax_percent

# Computes the sum of the subtotal discount (if applicable) and the sales tax amount
amount_due = initial_subtotal + sales_tax_amount

# Displays the total amount due
print(f"\nHaving a total of {quantity} items with an initial subtotal of ${initial_subtotal}, your bill details is:"
      f"\nDiscount Percentage: ${discount_percent}"
      f"\nDiscount Amount: ${discount_amount:.2f}"
      f"\nSales Tax Amount Default Percentage: ${sales_tax_percent}"
      f"\nSales Tax Amount: ${sales_tax_amount:.2f}"
      f"\nAmount Due: ${amount_due:.2f}")