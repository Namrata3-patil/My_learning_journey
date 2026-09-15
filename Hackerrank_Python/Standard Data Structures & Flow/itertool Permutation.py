
"""
>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
Task

You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.
Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""
from itertools import permutations

# Read input from STDIN and split by space
S, k = input().split()

# Convert k to an integer and sort the string S to ensure lexicographic order
k = int(k)
sorted_S = sorted(S)

# Generate and print permutations
for p in permutations(sorted_S, k):
    print(''.join(p))
