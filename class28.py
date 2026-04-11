'''
Keep It Private!
Outline:
Write a program to create a class with following variables and methods - 
1. Private variable named privateVar that contains an integer value
2. Create a private function privMeth that prints a message 
3. Create a function hello that prints the value of privateVar 4. 
Create an object for the class and call all the functions.


class myClass:
    #Private Variable
    __privateVar = 27;

    #Private method
    def __privMeth(self):
        print("I'm inside class myClass")


    #Function to print value
    def hello(self):
        print("Private Variable value: ", myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privMeth

Computer Price
Outline:
Write a program to create a class
 Computer with a private attribute 
 max_price and methods sell(to display)
the selling price and setmaxprice
(change the private attribute max_price). 
Now create an object for the class Computer.
 Try changing the value of max price and use the
 sell function to display the updated price. Use a 
setter function to update the value and again display the price.


class Computer : 
    def __init__(self):
        self.__maxprice = 900

    def sell (self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self , price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()

Point Function
Outline:
Write a program to create a class Point that consists of
 a constructor to set coordinates equal to x and y. Also, 
 it consists of a function that returns the coordinates in
 Point format.
 Create an object passing the coordinates and print the Point.
'''

class Point:
    def __init__(self , x=0 , y=0):
        self.x = x
        self.y = y


    def __str__(self):
        return "({0} , {1})".format(self.x , self.y)
    
p1 = Point(2,3)
print(p1)