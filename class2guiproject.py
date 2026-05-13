from tkinter import *
from tkinter import messagebox
from datetime import date

# Function to calculate age
def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birth_date = date(year, month, day)
        today = date.today()

        age = today.year - birth_date.year

        # Check if birthday has occurred this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Present Age: {age} Years")

    except:
        messagebox.showerror("Invalid Input", "Please enter a valid date!")

# Create main window
root = Tk()
root.title("Age Calculator")
root.geometry("350x300")
root.config(bg="lightblue")

# Heading
heading = Label(root, text="Age Calculator", font=("Arial", 18, "bold"), bg="lightblue")
heading.pack(pady=10)

# Day input
Label(root, text="Enter Day:", font=("Arial", 12), bg="lightblue").pack()
day_entry = Entry(root, font=("Arial", 12))
day_entry.pack(pady=5)

# Month input
Label(root, text="Enter Month:", font=("Arial", 12), bg="lightblue").pack()
month_entry = Entry(root, font=("Arial", 12))
month_entry.pack(pady=5)

# Year input
Label(root, text="Enter Year:", font=("Arial", 12), bg="lightblue").pack()
year_entry = Entry(root, font=("Arial", 12))
year_entry.pack(pady=5)

# Calculate button
calc_button = Button(root, text="Calculate Age", font=("Arial", 12, "bold"),
                     bg="green", fg="white", command=calculate_age)
calc_button.pack(pady=15)

# Result label
result_label = Label(root, text="", font=("Arial", 14, "bold"), bg="lightblue")
result_label.pack(pady=10)

# Run the application
root.mainloop()