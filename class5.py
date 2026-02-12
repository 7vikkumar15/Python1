'''Conditional statements
Outline:
write a program to check whether the given number is positive?




number=int(input("Enter the Number "))

if number > 0 :
     print("is a positive number")

else:
     print("is a negative number")
'''
'''
Profit loss
Outline:
Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?


actual_cost = float(input("Please Enter the Actual Product Price: "))
sale_amount = float(input(" Please Enter the Sales Amount: "))

if(sale_amount > actual_cost) :
     amount = sale_amount - actual_cost
     print("Total Profit = {0}" .format(amount))
else:
     print("No Profit !!!!!!")

''' 
'''
Checking the number greater or smaller
Write a program to check whether the given number is greater than 15 or smaller than 15.

i = int(input("enter the number : "))

if(i<15):
    print("i is smaller than 15")
    print("i'm in else block")

else :
    print("i is greater than 15 ")
    print("i'm in else Block")
    
print("i'm not in if and not in else block")
'''

'''
Odd-even
Outline:
Write a program to check whether the given number is even or odd?

'''

number = int(input("Enter Number to check: "))
print("Number to be checked : " , number)


if number %2==0 :
    print("This is an even number")

else :
    print("This is an odd number")






