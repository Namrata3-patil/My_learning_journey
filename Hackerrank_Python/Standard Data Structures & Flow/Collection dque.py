from collections import deque

d = deque()
for _ in range(int(input())):
  cmd = input().split()
  if cmd[0] == "append":
    d.append(cmd[1])
  elif cmd[0] == "appendleft":
    d.appendleft(cmd[1])
  elif cmd[0] == "pop":
    d.pop()
  elif cmd[0] == "popleft":
    d.popleft()

print(*d)

'''
Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2
'''
