# PROBLEM: Split a string into equal substrings of size k, remove duplicate 
# characters from each substring while maintaining order, and print each result.
# SOLUTION: Iterate through the string in steps of k to slice substrings. Use 
# a loop and a membership test ('not in') to keep only the first occurrence of each character.

def merge_the_tools(string, k):
    # Iterate through the string from index 0 to len(string) in steps of k
    for i in range(0, len(string), k):
        # Slice the string to get a substring of length k
        substring = string[i : i+k]
        
        # Initialize an empty string to store unique characters
        unique = ""
        
        # Loop through each character in the current substring
        for j in substring:
            # If the character hasn't been added yet, append it to preserve unique order
            if j not in unique:
                unique += j
                
        # Print the processed substring with duplicates removed
        print(unique)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
