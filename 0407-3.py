speed_limit = 30
try:
    speed = float(input("Enter the speed: "))
    if speed > speed_limit:
        print("Overspeed")
    else:
        print("Within speed limit")
except ValueError:
    print("Please enter a valid speed")
