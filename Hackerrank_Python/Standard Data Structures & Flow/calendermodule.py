# Enter your code here. Read input from STDIN. Print output to STDO
import calendar

# Read month, day, and year from standard input
month, day, year = map(int, input().split())

# Get the day of the week and print it in uppercase
print(calendar.day_name[calendar.weekday(year, month, day)].upper())
