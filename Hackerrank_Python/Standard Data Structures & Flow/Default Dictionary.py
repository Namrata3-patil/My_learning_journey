# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

# Read sizes of group A and group B
n, m = map(int, input().split())

# Initialize a defaultdict with list as default factory
d = defaultdict(list)

# Record 1-indexed positions of words in group A
for i in range(n):
    word = input()
    d[word].append(str(i + 1))

# Process group B and print results
for j in range(m):
    word = input()
    # If the word exists, print indices joined by space; otherwise print -1
    print(' '.join(d[word]) if word in d else '-1')
'''
Sample Input

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
Sample Output

1 2 4
3 5
Explanation

'a' appeared  times in positions ,  and .
'b' appeared  times in positions  and .
In the sample problem, if 'c' also appeared in word group , you would print .
'''
