print("Welcome to the Rollercoaster!")
height = int(input("How tall are you in cm? "))

if height >= 120:
    print("You're tall enough to ride!")

    age = int(input("How old are you? "))
    
    if age < 12:
        print("You're not old enough to ride!")
    elif age >= 70:
        print("Sorry its harmful for your health!")

    else:
        print("You're old enough to ride!")

    

else:
    print("Sorry, you'll have to get on a ride later.")
