a,b=map(int,input().split())
if a>b:
    g=b
else:
    g=a
dub=[]
for i in range(1,g+1):
    if a%i==0 and b%i==0:
        dub.append(i)
print(dub[-1])
