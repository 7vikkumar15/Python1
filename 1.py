import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        # Simple Interest
        simple_interest = (principal * rate * time) / 100

        # Compound Interest
        compound_amount = principal * ((1 + rate / 100) ** time)
        compound_interest = compound_amount - principal

        result_label.config(
            text=f"Simple Interest = {simple_interest:.2f}\n"
                 f"Compound Interest = {compound_interest:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Interest Calculator App")
root.geometry("400x350")

tk.Label(root, text="Principal Amount").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Rate of Interest (%)").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Time Period").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()

tk.Button(root, text="Calculate", command=calculate_interest).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()