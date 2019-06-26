n = int(input())
a = 0
b = 0
c = n
while c != 0:
    a = c%10
    b = (b*10)+a
    c = c//10
if(b==n):
    print('yes')
else :
    print('no')
