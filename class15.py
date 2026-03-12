'''Break
Outline:
Write a program to check alphabet “A” is present in the given string or not. And terminate the loop after finding the alphabet “A.”

a = input("Enter a word : ")

for i in a:
    if ( i == 'a'):
        print("A is found " , i)
        break
    else:
        print("A not found" , i)

'''

'''Pass
Outline:
Write a program to satisfy the following conditions of the given range: If the number is divisible by 20, it provides an output "twist." If the number is divisible by 15, it will pass (no output) If the number is divisible by 5, it will give an output “fizz.” If the number is divisible by 3, it will give an output "buzz." Otherwise, it will give the output of that number.

for x in range(21): 
    if x % 20 == 0:
     print("twist" , x)

    elif x % 15 == 0: 
      pass

    elif x % 5 == 0: 
     print("fizz" , x)

    elif x % 3 == 0:
      print("buzz" , x )
     
    else:
      print(x)
      
      
'''

'''Continue
Outline:
Write a program to display 1 to 10 numbers in reverse order and skip the number 5.
Project:'''

var = 10 
while var > 0:
    var = var-1
    if var == 5 :
        continue
    print("\n Current variable value : " , var )
print("\n Bye")