secret_num = 3
guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
    guess = int(input('Enter your guess :'))
    guess_count += 1
    if guess == secret_num:
        print('You won!')
        break
else :
    print('You losed the chance')
