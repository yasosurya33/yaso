sent=input()
sum = 0
for i in sent:
    if not i.isspace():
        if not i.isalnum():
            sum=sum+1
print(sum)
