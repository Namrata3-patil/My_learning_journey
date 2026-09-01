# Read the number of elements in the set
n = int(input())

# Read the space-separated elements, convert them to integers, and create a set
s = set(map(int, input().split()))

# Read the number of commands
num_commands = int(input())

# Loop through and execute each command
for _ in range(num_commands):
    # Split the command line into components
    command_input = input().split()
    command_name = command_input[0]
    
    # Execute the matching set operation
    if command_name == "pop":
        s.pop()
    elif command_name == "remove":
        s.remove(int(command_input[1]))
    elif command_name == "discard":
        s.discard(int(command_input[1]))

# Print the sum of the remaining elements in the set
print(sum(s))
