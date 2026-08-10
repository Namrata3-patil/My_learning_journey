# PROBLEM: Find the second-highest (runner-up) unique score from user input.
# SOLUTION: Convert the input to a set to remove duplicate top scores, sort in descending order, and grab index 1.

if __name__ == '__main__':
    # 1. Read the number of elements (n is a placeholder, not actively used below)
    n = int(input()) 
    
    # 2. Convert space-separated string input into a list of integers
    arr = list(map(int, input().split())) 
    
    # 3. Use set() to eliminate duplicate scores so the highest score only appears once
    unique_list = list(set(arr)) 
    
    # 4. Sort the unique scores from highest to lowest
    unique_list.sort(reverse=True) 
    
    # 5. Print the second element (index 1), which is the runner-up score
    print(unique_list[1]) 
