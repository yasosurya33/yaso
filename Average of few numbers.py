d=int(input())
num=list(map(int,input().split()))[:d]
sum=0
for i in num:
    sum+=i
print(sum//d)
