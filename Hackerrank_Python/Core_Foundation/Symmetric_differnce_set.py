#Given 2  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
# enter your code here. read input from stdin. print output to stdout

# Cleanly read the first size integer without printing anything
m = int(input()) 
a = set(map(int, input().split()))

# Cleanly read the second size integer without printing anything
n = int(input()) 
b = set(map(int, input().split()))

# Find symmetric difference elements
c = a.difference(b)
d = b.difference(a)

s = set()
s.update(c, d)

# Print each element on a new line (standard HackerRank format for Symmetric Difference)
for num in sorted(s):
    print(num)
