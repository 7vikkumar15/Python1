import tkinter as tk
from tkinter import ttk, messagebox


class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Order Management Application")
        self.root.geometry("800x600")

        self.menu_items = {
            "Pizza": 10.0,
            "Burger": 7.0,
            "Pasta": 8.0,
            "Salad": 5.0,
            "Strong Meal": 15.0
        }

        self.exchange_rate = 82

        self.setup_background()

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        # Menu items
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):

            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )
            label.grid(row=i, column=0, padx=10, pady=5)

            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)

            self.menu_quantities[item] = quantity_entry

        # Currency selection
        self.currency_var = tk.StringVar(value="USD")

        ttk.Label(
            frame,
            text="Select Currency:",
            font=("Arial", 12)
        ).grid(
            row=len(self.menu_items) + 1,
            column=0,
            padx=10,
            pady=5
        )

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "INR")
        )

        currency_dropdown.grid(
            row=len(self.menu_items) + 1,
            column=1,
            padx=10,
            pady=5
        )

        currency_dropdown.current(0)

        self.currency_var.trace_add(
            "write",
            self.update_menu_prices
        )

        # Order button
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )

        order_button.grid(
            row=len(self.menu_items) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )

    def setup_background(self):
        """Set background image"""
        try:
            self.bg_image = tk.PhotoImage(file="bg.png")

            background_label = tk.Label(
                self.root,
                image=self.bg_image
            )
            background_label.place(
                x=0,
                y=0,
                relwidth=1,
                relheight=1
            )

        except Exception:
            print("Background image (bg.png) not found.")

    def update_menu_prices(self, *args):
        currency = self.currency_var.get()

        symbol = "$" if currency == "USD" else "₹"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(
                text=f"{item} ({symbol}{price:.2f})"
            )

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n\n"

        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, quantity_entry in self.menu_quantities.items():
            quantity = quantity_entry.get()

            if quantity.isdigit():
                quantity = int(quantity)

                if quantity > 0:
                    price = self.menu_items[item] * rate
                    cost = quantity * price

                    total_cost += cost

                    order_summary += (
                        f"{item}: {quantity} x "
                        f"{symbol}{price:.2f} = "
                        f"{symbol}{cost:.2f}\n"
                    )

        if total_cost > 0:
            order_summary += (
                f"\nTotal Cost: "
                f"{symbol}{total_cost:.2f}"
            )
            messagebox.showinfo(
                "Order Placed",
                order_summary
            )
        else:
            messagebox.showwarning(
                "No Items",
                "Please enter quantity for at least one item."
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.mainloop()