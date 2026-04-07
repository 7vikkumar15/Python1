
'''

    def __init__(self , name , colour):
        self.name = name
        self.colour = colour

    def intro (self):
        print("Hello , I am " , self.name)
        print("I am in ", self.colour) 

apple = fruit("Apple" , "Red")
apple.intro()

class fruit:

    def __init__(self, name, color):
        self.name = name
        self.color = color

apple = fruit('Apple', 'Red')

print(apple.name)
 

l1 = ["eat" , "sleep" , "repeat"]

obj1 = enumerate (l1)
print(list(enumerate(l1)))

String Upper Case
Outline:
Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1.
 Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case.
 Next up create an object and call methods to get everything implemented.


class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter String : ")

    def print_String(self):
        print("Result is : " , self.str1.upper())

str1 = IOString()

str1.get_String()
str1.print_String()

Employee in and Out
Outline:
Write a program to create a class with the named employee and create a constructor and destructor.
 Then, write a function to create an object for that class and delete the object.
 Make sure you call the function to get everything implemented!

class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called")

def Create_obj():
    print('Making Object....')
    obj = Employee()
    print("Function end ....")
    return obj
print("Calling Create_Obj() Function...")
obj = Create_obj()
print("Program end ....")

Pair of Elements
Outline:
Write a Python program to create a class that will find the 
numbers in the tuple that add up to a sum and return the position 
of elements. The value of the sum can be taken as input from the user. 
Tuple - (10,20,30,40,50,60,70)

'''

class pair_elements:
    def twoSum(self , nums , target):
        lookup = {}

        for i , num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target-num] , i)
            lookup[num] = i

value = int(input("Enter sum for which you want to take this search: "))
print("index1=%d , index2=%d" % pair_elements().twoSum((10 , 20 , 30 , 40  , 50 , 60 , 70) , value))