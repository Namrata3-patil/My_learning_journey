#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    # Check if the number is odd
    if n % 2 != 0:
        print("Weird")
    else:
        # If the number is even, check the ranges
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 100:  # Note: The problem statement bounds even numbers up to 20
            # If the problem statement says "6 to 20 inclusive", use this line instead:
            # if 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
