from collections import deque
a,b=map(int,input().split())
queue = deque(list(input().split()))
for i in range(b):
    queue.appendleft(queue.pop())
for i in queue:
    print(i,end=" ")
