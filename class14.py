'''Tip, the waiter
Outline:
Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.
Project:

def total_calc(bill_amount , tip_perc):
    # define the function
    total = bill_amount*(1+0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ₹{total}")

total_calc(150 , 20)
'''
'''Cube of the cube
Outline:
Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3



#Define function to calculate cube
def cube (number):
    return number*number*number

#Define a function which will 
# execute cube function if the user entered number is divisible to 3

def by_three(number):
    if number %3 == 0:
        return cube(number)
    
    else :
        return  False
    
#Display Result
print(by_three(9))
print(by_three(4))

'''

'''Factorial
Outline:
Write a program to find the factorial using recursive function'''

def factorial (x):
    '''This is a function to find the factorial of an integer'''

    if x==0 or x ==1:
        return 1
    
    else:
        return x *factorial(x-1)
    
#Display Result
print(factorial.__doc__)

print("The factorial of 0 is", factorial(0))
print("The factorial of 1 is", factorial(1))
print("The factorial of 2 is", factorial(2))
print("The factorial of 3 is", factorial(3))
print("The factorial of 4 is", factorial(4))
print("The factorial of 5 is", factorial(5))
print("The factorial of 6 is", factorial(6))
print("The factorial of 7 is", factorial(7))
print("The factorial of 8 is", factorial(8))
print("The factorial of 9 is", factorial(9))