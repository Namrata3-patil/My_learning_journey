from collections import OrderedDict

# 1. Read the number of items
N = int(input())

# 2. Initialize the OrderedDict
items = OrderedDict()

# 3. Loop through each input line
for _ in range(N):
    # Split the input from the right side at the last space
    item_name, space, price = input().rpartition(' ')
    price = int(price)
    
    # 4. Update the total price for the item
    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

# 5. Print the output in the requested format
for item_name, net_price in items.items():
    print(item_name, net_price)
'''
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
'''
