from collections import deque
nam,t=input().split()
dub=deque()
for i in nam:
    dub.append(i)
for i in range(int(t)):
    dub.appendleft(dub.pop())
for i in dub:
    print(i,end="")
