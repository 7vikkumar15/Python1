# Taking range input from user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

squares = []
even_squares = []
odd_squares = []

# Creating list of squares
for num in range(start, end + 1):
    sq = num ** 2
    squares.append(sq)
    
    # Separating even and odd squares
    if sq % 2 == 0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)

# Display results
print("\nAll square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)