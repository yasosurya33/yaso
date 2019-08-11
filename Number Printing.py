num=int(input())
number=[]
while num>0:
    number.append(num%10)
    num=num//10
number.reverse()
for i in number:
    print(i,end=" ")
