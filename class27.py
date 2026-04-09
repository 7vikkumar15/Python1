'''Is this a bus?
Outline:
Write a Python program to implement Inheritance by creating a 
Parent Class Vehicle with a constructor that has details like 
name, maximum speed, and mileage. Then, create a Child Class 
Bus that inherits Class Vehicle. Finally, showcase Inheritance to
 display the details of the Vehicle Bus named - School Volvo.

class Vehicle:
    def __init__(self , name , maximum_speed , mileage):
        self.name = name
        self.maximum_speed = maximum_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.maximum_speed, "Mileage:",
School_bus.mileage)


Employee Inheritance
Outline:
Write a program to create a parent class Person (attributes - name, id number) with a 
method display to display the 
attributes. Next, create a child class 
Employee (attributes - name, id number, salary, post). Access the 
attributes of parent class
 in child class. Then, create an object for child class and 
call the display method to display the name and id number.



class GST:
    def __init__(self , name , id_number):
        self.name = name
        self.id_number = id_number


    def display(self):
        print(self.name)
        print(self.id_number)


class Tax(GST):
    def __init__(self , name , idnumber , salary , post):
        self.salary = salary
        self.post = post

        GST.__init__(self , name , idnumber)

a = Tax("Potato" , 390579 , 200000000000000000000000000000000 , 'CEO of 10 thousand companies')
a.display()

Super Penguin
Outline:
Write a program to
 create a base class
   Bird, with a constructor 
   and two methods. Then,
     create a child class 
     that inherits the constructor 
     from Class Bird and has two functions. Finally,
       display how you can use Super to
 access the parent cl
 ass constructor inside the child class.

'''

class Bird:

    def _init_(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    def _init_(self):
# call super() function
        super() .__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

# Object Creation
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
    