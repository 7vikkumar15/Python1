# function to calculate circumference
def circumference(radius):
    pi = 3.14
    c = 2 * pi * radius
    return c

# taking input
r = float(input("Enter radius: "))

# calling function
result = circumference(r)

# printing result
print("Circumference of the circle is:", result)