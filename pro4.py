nam1, nam2 = map(str, input().split())
sum = 0
if len(nam1) > len(nam2):
    nam1, nam2 = nam2, nam1
a = 0
while a < len(nam1):
    sum += (ord(nam2[a]) - ord(nam1[a]))
    a += 1
for a in range(a, len(nam2)):
    sum += ord(nam2[a]) - ord('a') + 1
print(sum)
