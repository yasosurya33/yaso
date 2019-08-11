a = int(input())
b=list(map(int,input().split()))[:a]
b.sort()
for i in range(a):
    print(b[i],end=" ")
