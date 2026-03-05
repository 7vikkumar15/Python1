
def well_wishes():
     '''
    
    print ("Hello")
    print(("How are you ?"))

well_wishes()

def weather_condition():
    print("The weather is pleasent in : " , spring)
    print("The weather is the same in" , autumn)

spring="autumn"
autumn = spring

weather_condition()

'''

'''Calculator'''

def add ( P , Q )  :
     #For addition
     return P +Q

def subtract ( P , Q )  :
     #For subtraction
     return P  - Q

def multiply ( P , Q )  :
     #For multiply
     return P * Q

def divide ( P , Q )  :
     #For divide
     return P / Q

#Inputs from user

print("Please select the operation")
print("(a). Add")
print("(b). Subtract")
print("(c). Multiply")
print("(d). Divide")

choice = input("Please enter the choice (a/b/c/d):  ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':
    print(num_1 , "+", num_2 , "=", add(num_1 , num_2))

elif choice == 'b':
     print(num_1 , "-", num_2 , "=", subtract(num_1 , num_2))

elif choice == 'c':
     print(num_1 , "*", num_2 , "=", multiply(num_1 , num_2))

elif choice == 'd':
     print(num_1 , "/", num_2 , "=", divide(num_1 , num_2))

else:
     print("This is an invalid input")