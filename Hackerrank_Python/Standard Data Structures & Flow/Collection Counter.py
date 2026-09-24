'''
 is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.
'''
from collections import Counter

# Read the total number of shoes (not strictly needed for logic, but part of input)
num_shoes = int(input())

# Read the shoe sizes available in the shop and convert them to a list of integers
shoe_sizes = list(map(int, input().split()))

# Create a Counter dictionary to keep track of the available stock for each shoe size
inventory = Counter(shoe_sizes)

# Read the number of customers
num_customers = int(input())

# Initialize the total earnings variable
total_earnings = 0

# Process each customer's request
for _ in range(num_customers):
    size, price = map(int, input().split())
    
    # Check if the desired shoe size is in stock
    if inventory[size] > 0:
        total_earnings += price  # Add the price to total earnings
        inventory[size] -= 1     # Reduce the available stock by 1

# Print the total amount of money earned
print(total_earnings)
