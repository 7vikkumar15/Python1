# Program to check if age is between 10 and 20 using nested if

age = int(input("Enter your age: "))

if age >= 10:
    if age <= 20:
        print("Age is between 10 and 20 years.")
    else:
        print("Age is not between 10 and 20 years.")
else:
    print("Age is not between 10 and 20 years.")