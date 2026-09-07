"""
Task
Read in two integers, a and b, and print three lines.
The first line is the integer division  (While using Python2 remember to import division from __future__).
The second line is the result of the modulo operator: .
The third line prints the divmod of a and b
Input (stdin)
177
10
Expected Output
17
7
(17, 7)
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
b=int(input())
print(a//b)
print(a%b)
print(divmod(a,b))
