import math

# Taking input from user (in degrees)
angle = float(input("Enter angle in degrees: "))

# Convert degrees to radians
radians = math.radians(angle)

# Calculate values
sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

# Display results
print("Sin(", angle, ") =", sin_value)
print("Cos(", angle, ") =", cos_value)
print("Tan(", angle, ") =", tan_value)