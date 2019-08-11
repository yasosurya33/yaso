a = int(input())
b=list(map(int,input().split()))[:a]
b.sort()
print(b[a//2])
