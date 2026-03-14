try:
    age = int(input("Enter your age: "))

    if age <= 0 or age > 120:
        print("Invalid age entered")
    else:
        print("Age entered is correct")

        if age % 2 == 0:
            print("Age is Even")
        else:
            print("Age is Odd")

except:
    print("Error: Please enter numbers only")