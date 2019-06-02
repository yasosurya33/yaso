weight = int(input('Weight:'))
output = input('P or L')
if output.upper()=='L':
    kg = weight * 0.45
    print(f'Your weigth is {kg} kgs')
elif output.upper()=='P':
    kg = weight/0.45
    print(f'Your weigth is {kg} pounds')
