# PROBLEM: Print decimal, octal, hexadecimal, and binary values from 1 to n.
# SOLUTION: Use built-in string conversion functions, strip prefixes, and right-justify each column using the width of the largest binary number.

def print_formatted(number):
    # 1. Determine padding width using the length of the binary string of the maximum number
    width = len(bin(number)[2:])
    
    # 2. Iterate from 1 up to and including 'number'
    for i in range(1, number + 1):
        # 3. Convert integer to standard string formats and slice off Python prefixes (e.g., '0o', '0x', '0b')
        decimal = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()  # Hexadecimal characters must be capitalized
        binary = bin(i)[2:]
        
        # 4. Print all four values right-justified to match the maximum width
        print(decimal.rjust(width), octal.rjust(width), hexa.rjust(width), binary.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
