import tkinter as tk
from tkinter import ttk, messagebox

class RestruantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restruant Management App")

        self.menu_items = {
            "Pizza" : 12,
            "Burger" : 9,
            "Fries" : 5,
            "Sprite" : 7,
            "Coffee" : 3,
            "Tea" : 3
        }

        frame = ttk.Frame(root)
        frame.place(relx = 0.5, rely =0.5, anchor= tk.CENTER)

        ttk.Label(frame, text= "Restruant Order Management", font = ("Arial", 20, "bold" )
        ).grid(row=0, columnspan=3, padx = 10, pady = 10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text = f"{item} (${price}):",
                font=("Arial", 12)
            )
            label.grid(row=i, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        order_button = ttk.Button(
            frame,
            text = "Place Order",
            command = self.place_order
        )

        order_button.grid(
            row=len(self.menu_items) + 2,
            columnspan = 3,
            padx=10,
            pady=10  
        )
    
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"

        symbol = "$"

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item]
                cost = quantity * price
                total_cost += cost
                if quantity>0:
                    order_summary += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"

        if total_cost>0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("OrderPlaced", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least 1 item")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestruantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()