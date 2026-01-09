ride = input("Choose between 1, Bike, or 2, Car")

if ride == "1":
    bikeride = input("Choose Between 1, scooter, 2, motorcycle")
    if bikeride == "1":
        print("You have chosen Scooter")
    else:
        print("You have chosen Motorcycle")

elif ride == "2":
    carride = input("Choose between 1, Honda, 2, Toyota")
    if carride == "1":
        print("You have chosen Honda")
    else:
        print("You have chosen Toyota")

else:
    print("Invalid answer")


