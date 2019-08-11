a = int(input())
list=list(map(int,input().split()))[:a]
list.sort()
print(list[-1])
