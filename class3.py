'''Data types
Outline:
Write a program to find what type of datatype the given variable is?'''
'''
# Let's check the datatype of different values

a=5
print("type of a: " , type(a))

b=2.5
print("type of b: " , type(b))

c=True
print("type of c: " , type(c))

d="Coding"
print("type of d: " , type(d))

'''

'''
Typecasting
Outline:
Write a program to change the datatype of given variables?
#Assigning Different Variables

name = "Penguin"
age=15
is_student=True
weight=38.5

print("Name :", name)
print("Data Type of name is", type(name))

print("Age :", age)
print("Data Type of Age is", type(age))

print("is_student :", is_student)
print("Data Type of is_student is", type(is_student))

print("weight :", weight)
print("Data Type of weight is", type(weight))

#Type casting to convert the data type of vaiables

print("\n After Type Casting .....")
age = str(age)
print(age)
print("Data Type of age is" , type(age))
weight = int(weight)
print(weight)
print("Data Type of Weight is", type(weight))
name1=bool(name)
print(type(name1))
'''
'''
#Input a word

text=str(input("Enter a string : "))
#Reverse String
#using step value as -1 to iterate in reverse

revText = text[::-1]
text = revText


print("Reverse of given String is :")
print(text)

'''

a="Psychology"

print(a[5::9])

