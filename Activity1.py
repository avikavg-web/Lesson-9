medical = input("Do you have any medical cause?")


if medical == "No":
    attend = input("What is your attendance")
    if attend >= "75":
        print("You are allowed to take the exam")
    else:
        print("You are not allowed to take the exam")
else:
    print("You are allowed to take the exam")
   


