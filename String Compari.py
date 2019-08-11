s,k=input().split()
if len(s)>len(k):
    print(s)
elif len(s)==len(k):
    print(k or s)
else :
    print(k)
