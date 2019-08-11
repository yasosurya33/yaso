b,c = input().split()
for num in range(int(b)+1,int(c)):
   if num>1:
       for i in range(2,num):
           if num%i==0:
               break
       else :
           print(num)
