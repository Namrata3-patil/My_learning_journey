# Read the number of test cases
num_test_cases = int(input())

for _ in range(num_test_cases):
    # Read set A
    size_a = int(input())
    set_a = set(map(int, input().split()))
    
    # Read set B
    size_b = int(input())
    set_b = set(map(int, input().split()))
    
    # Check if A is a subset of B
    print(set_a.issubset(set_b))

"""
Input (stdin)
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Expected Output
True
False
False
"""
