command = ""
car_started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if car_started == True:
            print("Car is already started")
        else:
            print("Car started...Ready to go!")
            car_started = True
    elif command == "stop":
        if car_started == False:
            print("Car is already stopped")
        else:
            print("Car stopped.")
            car_started = False
    elif command == "help":
        print("""
start - to star the car
stop - to stop the car
quit - to exit""")
    elif command == "quit":
        break
    else:
        print("I don't understand that")