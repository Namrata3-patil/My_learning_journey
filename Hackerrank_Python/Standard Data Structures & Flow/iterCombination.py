"""
Input Format

A single line containing the string  and integer value  separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
"""
from itertools import combinations

# Read the space-separated input string and integer
S, k = input().split()

# Sort the string lexicographically first to ensure 
# combinations are emitted in sorted order
sorted_S = sorted(S)

# Generate and print combinations for each size from 1 up to k
for size in range(1, int(k) + 1):
    for combo in combinations(sorted_S, size):
        print("".join(combo))
