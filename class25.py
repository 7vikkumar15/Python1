'''
Student Class
Outline:
Write a program to create a class with the name Student and perform the following tasks - 1. Declare a variable grade 2. Print a sentence inside the class 3.
 Create an object of class student and see the output
class student:
    grade = 10
    print("Hi I am a student of grade" , grade)

ob = student()

Class Vehicle
Outline:
Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object

#Create class
class Vehicle:
    #Create init method
    def __init__(self,max_speed,mileage):

        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240 , 18)

#print

print("Model Max Speed: " , modelX.max_speed)
print("Model Mileage: " , modelX.mileage)

Class Parrot
Outline:
Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well

'''


# create class
class Parrot:
    # class attribute
    species = "bird"


# instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Instaniate the parrot class

kai = Parrot("kai" , 10)
tax = Parrot("tax" , 10.000)

print("Kai is a {}".format(kai.species))
print("Tax is a {}".format(tax.species))

print("{} is {} years old".format(kai.name , kai.age))
print("{} is {} years old".format(tax.name , tax.age))
