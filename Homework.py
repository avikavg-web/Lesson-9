age = int(input("How old are you"))

if age <= 100:
    if age >= 10:
        if age <= 20:
            print("Your age is inbetween 10 and 20")
        else:
            print("No")
    else:
        print("You are either younger than 10, or more than 20")
else:
    print("Invalid")
