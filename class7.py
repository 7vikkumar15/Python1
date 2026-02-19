'''Exam Eligibility Check
Outline:
Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance
 If attendance is above 75, then allowed; otherwise, not allowed.

medical_cause = input("Did you have a medical cause ? (Y/N): ").strip().upper()

#Checking the user input and predicting output accordingly

if medical_cause == 'Y':
    print('You are allowed')
else :
    # Take input of the attendence
    atten = int(input('Enter the attendence of the student: '))

    if atten >= 75:  # Conditional statement
        print('Allowed')
    else:
        print('Not Allowed')
    
'''


'''Electricity bill
Outline:
Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200
. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.


units=int(input('Enter units consumed: '))

if units < 50:
    tax=25
    amount= units * 2.60 + tax
    print('Your electricity bill is :  ', amount )


elif units < 100:
    tax=35
    amount= units * 3.25 + tax
    print('Your electricity bill is :  ', amount )


elif units < 200:
    tax=45
    amount= units * 5.26 + tax
    print('Your electricity bill is :  ', amount )


else:
   
    tax=75
    amount= units * 8.45 + tax
    print('Your electricity bill is :  ', amount )
'''

print("Select your choice")
print("1 . Bike")
print("2 . Cars")


#Take input

choice = int(input("Enter your choice: "))


if (choice == 1): 
    print("What type of bike ??")
    print("1. Ultravoillete")
    print("2. Yamaha")

    choice2 =int(input("Enter your choice: "))
    if choice2==1 :
        print("You have selected Ultravoillete")
    else:
        print("You have selected Yamaha")


elif (choice == 2): 
    print("What type of car ??")
    print("1. SUV")
    print("2. Coupe")

    choice2 =int(input("Enter your choice: "))
    if choice2==1 :
        print("You have selected SUV")
    else:
        print("You have selected Coupe")