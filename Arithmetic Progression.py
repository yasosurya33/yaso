n,a,d = input().split()
i=0
sum=0
while i < int(n) :
    sum += int(a)
    a = int(a) + int(d)
    i += 1
print(sum)
