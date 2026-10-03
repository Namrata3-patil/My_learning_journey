import calendar

# Read the space-separated month, day, and year from input
month, day, year = map(int, input().split())

# Get the day of the week index (0 = Monday, 6 = Sunday)
day_index = calendar.weekday(year, month, day)

# Look up the day name in uppercase from the calendar day_name array
day_name = calendar.day_name[day_index].upper()

print(day_name)
'''
Sample Input

08 05 2015
Sample Output

WEDNESDAY
Explanation

The day on August 5th 2005 was WEDNESDAY
'''
