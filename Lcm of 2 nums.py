a,b=map(int,input().split())
if a%b==0:
    print(a)
elif b%a==0:
    print(b)
else:
    print(a*b)
