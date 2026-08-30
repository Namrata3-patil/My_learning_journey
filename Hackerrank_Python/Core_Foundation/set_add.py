# Problem: Count the total number of unique country stamps in a collection.
# Input: The first line contains total stamps (N), followed by N country names.
# Output: Print the total number of distinct/unique countries.

N = int(input())
names_set = set()

for _ in range(N):
    # input() reads the line as a string; stripping removes trailing newlines/spaces
    names_set.add(input().strip())

print(len(names_set))
