access = input()
if access.upper() =="HELP":
    command = input('start - to start the car \nstop - to stop the car\nquit to exit ')
    while command.upper() != "QUIT" :
        command_given = input('>')
        if command_given.upper() == "START" :
            print('The car is started')
        elif command_given.upper() == "STOP" :
            print('The car is stopped')
        elif command_given.upper() == "QUIT" :
            break
        else :
            print("I don't understand that")
else:
    print("I don't understand")
