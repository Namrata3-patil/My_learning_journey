#!/bin/python3

import math
import os
import random
import re
import sys



from collections import Counter

# Read input string from standard input
s = input().strip()

# Count the frequency of each character
frequency = Counter(s)

# Sort by frequency (descending) and then alphabetically (ascending)
sorted_characters = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

# Print the top 3 most common characters
for char, count in sorted_characters[:3]:
  print(f"{char} {count}")
  '''
  • Counter(s): Counts how many times each character appears in the string.
• key=lambda x: (-x[1], x[0]):
	• -x[1] sorts the counts in descending order (highest count first).
	• x[0] sorts the characters alphabetically (A to Z) if two characters share the same count.
• [:3]: Selects and prints only the top 3 characters.
Sample Input 0

aabbbccde
Sample Output 0

b 3
a 2
c 2
'''
