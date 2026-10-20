# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

for _ in range(int(input().strip())):
    n = int(input().strip())
    deq = deque(map(int, input().strip().split()))
    
    # The first picked cube can be the larger of the two ends
    prev = max(deq[0], deq[-1])
    possible = True
    
    while deq:
        if prev >= deq[0] and prev >= deq[-1]:
            if deq[0] >= deq[-1]:
                prev = deq.popleft()
            else:
                prev = deq.pop()
        else:
            possible = False
            break
            
    print("Yes" if possible else "No")
