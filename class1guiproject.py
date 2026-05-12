from tkinter import *

# Function to calculate product
def calculate_product():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    product = num1 * num2
    result_label.config(text="Product = " + str(product))

# Create window
root = Tk()
root.title("Product Calculator")
root.geometry("300x200")

# Labels
Label(root, text="Enter First Number").pack(pady=5)
entry1 = Entry(root)
entry1.pack(pady=5)

Label(root, text="Enter Second Number").pack(pady=5)
entry2 = Entry(root)
entry2.pack(pady=5)

# Button
Button(root, text="Find Product", command=calculate_product).pack(pady=10)

# Result Label
result_label = Label(root, text="")
result_label.pack(pady=5)

# Run window
root.mainloop()