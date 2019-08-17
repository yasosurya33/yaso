num, num1=input().split()
a=abs(len(num1) - len(num))
for i in range(len(num)):
  if(len(num1)==1 and num1[i] in num):
    break
  if(num[i]!=num1[i]):
    a= a + 1
print(a)
