car_condition = "stop"
command = ""
while True:
    command = input('> ').lower()
    if command == 'help':
        print('''
start - to start the car
stop - to stop the car
exit - to exit
        ''')
    elif command == 'start':
        if car_condition == 'start':
            print("Car already started... Don't do that.")
        else:
            print('Car started... Ready to go')
    elif command == 'stop':
        if car_condition == 'stop':
            print("Car already stopped... Don't do that.")
        else:
            print('Car stopped')
    elif command == 'exit':
        break
    else:
        print("I didn't understand that")
    car_condition = command
