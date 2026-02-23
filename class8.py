#for i in range(11):
 #   print(i)
'''
for i in range(5 , 100 , 5):
    print(i)'''
'''
for i in "pneumonoultramicroscopicsilicovolcanoconiosis":
    print(i)

Sum of whole numbers
Outline:
Write a program to calculate the sum of whole numbers.


n = int(input("Enter the number whose sum you want to find: ") )
sum=0

for i in range(1 , n+1):
    sum = sum + i
print("\nSum = " , sum)

Reverse a String
Outline:
Write a program to reverse the string entered by the user.

string = input("Please Enter your own string : ")

string2 = ("")
for i in string:
    string2 = i + string2

print("\n The Orignal String = " , string)
print("\n Reversed String = " , string2)

reverse order
Outline:
Write a program to print the numbers in reverse order beginning from the number entered by the user.

n = int(input("Enter the value of n: "))

print("Numbers from {0} to {1} are : ".format(n,1))

for i in range (n,0,-1):
    print(i)
    '''