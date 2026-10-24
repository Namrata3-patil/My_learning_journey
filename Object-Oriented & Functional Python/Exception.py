for i in range(int(input())):
  try:
    values = input().split()
    print(int(values[0]) // int(values[1]))
  except ZeroDivisionError as e:
    print("Error Code:", e)
  except ValueError as e:
    print("Error Code:", e)

'''
Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
Note:
For integer division in Python 3 use //.
'''
