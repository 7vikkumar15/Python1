# 1. Squares of numbers
squares = [x**2 for x in range(1, 11)]

# 2. Even numbers
evens = [x for x in range(1, 21) if x % 2 == 0]

# 3. Odd numbers
odds = [x for x in range(1, 21) if x % 2 != 0]

# 4. Convert to uppercase
words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]

# 5. Names starting with 'a'
names = ["amit", "rahul", "ankit", "sumit"]
a_names = [name for name in names if name.startswith('a')]

# 6. Multiples of 3
multiples_of_3 = [x for x in range(1, 31) if x % 3 == 0]

# 7. Length of each word
lengths = [len(word) for word in words]

# 8. Replace negatives with 0
nums = [5, -3, 7, -1, 0]
no_negatives = [x if x >= 0 else 0 for x in nums]

# 9. Flatten nested list
nested = [[1, 2], [3, 4], [5]]
flat_list = [num for sublist in nested for num in sublist]

# 10. Create pairs
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
pairs = [(x, y) for x in list1 for y in list2]

# Printing all results
print("Squares:", squares)
print("Even numbers:", evens)
print("Odd numbers:", odds)
print("Uppercase words:", upper_words)
print("Names starting with 'a':", a_names)
print("Multiples of 3:", multiples_of_3)
print("Word lengths:", lengths)
print("No negatives:", no_negatives)
print("Flattened list:", flat_list)
print("Pairs:", pairs)