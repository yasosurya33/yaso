a = int(input())
b=list(map(int,input().split()))[:a]
for i in range(a):
    print(b[i],b.index(b[i]))
