"""
Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output

206
Explanation

Picking  from the st list,  from the nd list and  from the rd list gives the maximum  value equal to % = .
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

# Read K and M from the first line
k, m = map(int, input().split())

# Read the subsequent K lines, ignoring the first integer (number of elements)
lists = []
for _ in range(k):
    # row[0] is N_i, row[1:] are the actual elements
    row = list(map(int, input().split()))
    lists.append(row[1:])

# Compute the maximum possible value using Cartesian product
max_value = 0
for combination in itertools.product(*lists):
    # Calculate sum of squares modulo M for the current combination
    current_sum = sum(x**2 for x in combination) % m
    if current_sum > max_value:
        max_value = current_sum

# Output the maximum result
print(max_value)
