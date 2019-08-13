num=input()
if num.isnumeric:
    print("INT")
elif int(abs(num))+int(num)==0:
    print("INT")
else:
    print("LONG")
