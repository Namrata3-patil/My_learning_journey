# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    # Create a tuple from the input integers
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    
    # Print the hash value
    print(hash(t))
"""
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of 
"""
