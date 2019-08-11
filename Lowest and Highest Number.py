d=int(input())
num=list(map(int,input().split()))[:d]
num.sort()
print(num[0],num[-1])
