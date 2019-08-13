a,b=map(int,input().split())
sum=0
for i in range(a,b+1):
    for j in range(i+1):
        if i==j*j:
            sum+=1
print(sum)
