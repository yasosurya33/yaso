i = int(input())
c=list(map(int,input().split()))[:i]
c.sort()
for a in range(i):
    print(c[a],end=" ")
