"""
Sample Input

4 
a a c d
2
Sample Output

0.8333
Explanation

All possible unordered tuples of length  comprising of indices from  to  are:


Out of these  combinations,  of them contain either index  or index  which are the indices that contain the letter ''.

Hence, the answer is .
"""
from itertools import combinations

# Read input
n = int(input())
letters = input().split()
k = int(input())

# Find 1-based indices that contain the letter 'a'
target_indices = [i + 1 for i, char in enumerate(letters) if char == 'a']

# Generate all possible combinations of K indices from 1 to N
all_combinations = list(combinations(range(1, n + 1), k))

# Count combinations containing at least one target index
favorable_count = 0
for comb in all_combinations:
  if any(idx in target_indices for idx in comb):
    favorable_count += 1

# Calculate probability
probability = favorable_count / len(all_combinations)

# Print output correct up to 3 decimal places
print(f'{probability:.4f}')
