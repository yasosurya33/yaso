k,n = map(int,input().split())
x = list(map(int,input().split()))
res = 0
for i in range(n):
    res = res + x[i]
print(res)
