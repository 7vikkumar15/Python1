'''Value Error
Outline:
Write a program to understand how the value error exception works?

#Using try and except
try :
    number = int(input("Enter a number: "))
    print("The number entered is", number)

except ValueError as ex:
    print("Exception: " ,ex)
    '''

'''Multiple exceptions
Outline:
Write a program to check how the exceptions and finally statement works

try :
    num1 , num2 = eval(input("Enter 2 numbers , seprated by a comma : "))
    result = num1/num2
    print("Result is" , result)

#Using multiple except block for different type of error

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
     print("Comma is missing enter numbers like this 1 , 2  !!")

except:
    print("Wrong input")

else:
    print("No Exceptions")

finally:
    print("This will execute no matter what")
    '''

'''Bye Bye
Outline:
Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.'''

valid = False 
while not valid:
    try:
        n=int(input("Enter the number: "))
        while n%2==0:

            print("Bye")
            valid = True
    except ValueError:
        print("Invalid")

