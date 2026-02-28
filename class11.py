'''Right angle triangle
Outline:
Write a program to demonstrate a right angle triangle pattern?


print("Half Pyramid Pattern of Stars (*):")
n = int(input("enter the number of rows: "))

for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()
    '''
'''Floyd’s triangle
Outline:
Write a program to demonstrate a Floyd triangle pattern?

rows = int(input("Please Enter the total number of rows : "))
number = 1

print("Floyd's Triangle")

for i in range (1,rows + 1):
    for j in range(1,i+1):
        print(number , end = "  ")
        number = number +1
    print()
    '''
'''Diamond Pattern
Outline:
Write a program to demonstrate the numbers in a diamond pattern?'''

rowSize = int(input('Enter the no. rows : '))

if rowSize%2==0:
    halfDiamRow = int(rowSize/2)
else:
    halfDiamRow = int(rowSize/2)+1
space = halfDiamRow-1
#Loop upper part
for i in range(1 , halfDiamRow+1):
    for j in range(1,space+1):
        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
#Increment number at column
        num = num+1
    print()
space=1

#Lower
for i in range(1,halfDiamRow):
    for j in range(1,space+1):
        print(end=" ")
    space = space+1
    num = 1
    for j in range(1,2*(halfDiamRow-i)):
        print(end=str(num))
        num = num+1
    print()


    
