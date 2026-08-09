"""
Problem: Determine if a given year is a leap year in the Gregorian calendar.
Rules:
- A year is a leap year if it is evenly divisible by 4.
- However, if it is divisible by 100, it is NOT a leap year, 
  UNLESS it is also evenly divisible by 400.

Solution: Use conditional logic to check if the year is divisible by 4 
and not 100, OR if it is directly divisible by 400.
"""

def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
        
    return leap

year = int(input())
print(is_leap(year))
