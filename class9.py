'''Sum of Natural Numbers
Outline:
Write a program to find the sum of natural numbers.
n = int(input("Enter the number whose sum you want to find: ") )
sum=0
i = 1

while i<=n:
    sum = sum+i
    i = i+1

print("\nSum = " , sum)
'''

'''Infinity
Outline:
Write a program to check the infinite loop?
Project:

i = 0
while i<=0:
    print("I WILL RUN FOREVER")
'''

'''Armstrong number
Outline:
Write a program to check if the number entered by the user is an Armstrong number or not?'''

num=int(input("Enter the number : "))

#Intialize
sum=0

#Find the cube of the of each digit
temp=num
while temp > 0:
    #Digit = Last digit of input {eg - 75}=(digit - 5)
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

#Displa = result

if num == sum:
    print(num, "Is an Armstrong Number")
else:
    print(num, "Is not an Armstrong Number")
    