import math
num1, num2=map(int, input().split())
sam=[]
sam1=list(map(int, input().split()))
for i in range(0, num2):
    l1,h1=map(int,input().split())
    sam.append([l1, h1])
for i in sam:
    s1= i[0] - 1
    s2= i[1] - 1
    print(math.gcd(sam1[s1], sam1[s2]))
