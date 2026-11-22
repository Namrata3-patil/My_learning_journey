cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a, b = 0, 1
    cube=[]
    for _ in range(n):
       cube.append(a)
       a,b = b,a+b
    return cube
    
# Example: Print the first 7 terms

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

'''
Sample Input
5
Sample Output
[0, 1, 1, 8, 27]
O(N)
'''
