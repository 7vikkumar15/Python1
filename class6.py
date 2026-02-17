'''AND-OR operator
Outline:
Write a program to check whether the given values have boolean values or not.

a=10
b=12
c=0

if a and b and c :
    print("All numbers have boolean value as True")
else:
    print('Atleast one number has a value as false')
   

a=10
b=-10
c=0

if a > 0 or b>0:
    print("Either number is grater than 0")
else:
    print("No Number is greater than 0")



if b>0 or c>0:
    print("Either numberis grater than 0")
else:
    print("No Number is greater than 0")
 '''

'''NOT Equal Operator
Outline:
Write a program to check the application of not equal operator


A=10
B=12
C=12
print(A!=B)
print(B!=C)

a="python"
b = "coding"


if a !=b :
    print(a , 'and' , b ,' are diffferent')


a=4
b=5

if(a==1) != (b==5) :
    print("Hello")


a= int(input("Enter a number  "))

if a%2 != 0 :
    print(a, "Is not even number.")
'''


height = float(input('Enter your height in cm :' ))
weight = float(input("Enter your weight in kg :"))

BMI = weight / (height/100)**2

print("Your BMI is " , BMI)


if BMI <= 18.4:
    print("You are underweight.")

elif BMI <= 24.9:
    print("You are healthy")

elif BMI <= 29.9:
    print("You are Over-Weight")

elif BMI <= 34.9:
    print("You are Severely Over-Weight")

elif BMI <= 39.9:
    print("You are Obese")
else:
    print("You are Severely Over-Weight and Obese")