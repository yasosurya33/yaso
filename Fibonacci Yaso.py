num=int(input())
i=1
first=0
sec=1
while i <= num:
    if i<=1:
        fin=i
    else:
        fin=first+sec
        first=sec
        sec=fin
    print(fin)
    i+=1
