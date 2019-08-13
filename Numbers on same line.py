sam=[]
for i in range(3):
    sam.append(list(input().split()))
lab=0
for i in range(2):
    for j in range(1):
        if not sam[i][j] == sam[i+1][j] and not sam[i][j+1] == sam[i+1][j+1] and not sam[i][j] == sam[i][j+1]:
            lab=1
if not lab == 1:
    print("yes")
else:
    print("no")
