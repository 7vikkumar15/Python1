# Program to calculate due amount

# taking bill amount from user
bill_amount = float(input("Enter the total bill amount: "))

# taking paid amount from user
paid_amount = float(input("Enter the amount paid by the customer: "))

# calculating due amount
due_amount = bill_amount - paid_amount

# displaying result
print("The due amount is:", due_amount)