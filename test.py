
userAge = int(input("Enter your age: "))

def myfun():
    if userAge>= 18:
        print("You can Drive and Vote")
    elif userAge >= 16:
        print("You can Vote!")

    elif userAge >= 12:
        print("You are a adult, wait !")
    elif userAge >= 6:
        print("You are a kid, let`s wait for your turn! ")
    elif userAge >= 4:
        print("you are a baby, go have some sleep")
    else:
        print("You can't either Vote nor Drive")

myfun()