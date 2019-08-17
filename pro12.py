num1, num2=map(int, input().split())
nam=list(map(int, input().split()))
dub=[]
for i in range(0, num2):
     a,b=map(int,input().split())
     dub.append([a, b])
for i in range(num2):
     lower=dub[i][0]
     upper=dub[i][1]
     x=sum(nam[lower - 1:upper])
     print(x)
