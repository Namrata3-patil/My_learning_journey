def average(array):
    # Problem: Calculate the average of the unique numbers in a given list.
    # Solution: Convert the list to a set to remove duplicate values, 
    # then divide the sum of these unique elements by their total count.
    con = set(array)

    result = sum(con)/len(con)
    
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
