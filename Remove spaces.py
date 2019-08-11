t=input()
dup=[""]
for i in t:
    dup.append(i)
count=dup.count(" ")
for i in range(count):
    dup.remove(" ")
for j in dup:
    print(j,end="")
