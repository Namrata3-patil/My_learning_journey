# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    # Read the operation name and length (e.g., "update 2")
    op, length = input().split()
    
    # Read the elements of the other set
    other_set = set(map(int, input().split()))
    
    # Check the operation name and apply it with the other set
    if op == "intersection_update":
        A.intersection_update(other_set)
    elif op == "update":
        A.update(other_set)
    elif op == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)
    elif op == "difference_update":
        A.difference_update(other_set)

print(sum(A))
