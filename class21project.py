test_dict = {"a": 5, "b": 3, "c": 5, "d": 2}

value = int(input("Enter value to check: "))

count = list(test_dict.values()).count(value)

print("Frequency:", count)