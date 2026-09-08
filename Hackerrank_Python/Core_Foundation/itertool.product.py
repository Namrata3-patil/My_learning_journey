# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
"""

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
"""
# Read the space-separated elements for lists A and B
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute the cartesian product
cartesian_product = product(A, B)

# Print the space-separated tuples
print(*cartesian_product)
