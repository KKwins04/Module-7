import tkinter as tk
from datetime import date

def calculate_age():
    try:
        d = int(day_entry.get())
        m = int(month_entry.get())
        y = int(year_entry.get())

        today = date.today()
        age = today.year - y

        if (today.month, today.day) < (m, d):
            age -= 1

        result_label.config(text=f"Your age is: {age}")

    except ValueError:
        result_label.config(text="Please enter valid numbers!")

# Create window
window = tk.Tk()
window.title("Age Calculator")
window.geometry("300x250")

# Labels and entries
tk.Label(window, text="Day").pack()
day_entry = tk.Entry(window)
day_entry.pack()

tk.Label(window, text="Month").pack()
month_entry = tk.Entry(window)
month_entry.pack()

tk.Label(window, text="Year").pack()
year_entry = tk.Entry(window)
year_entry.pack()

# Button
tk.Button(window, text="Calculate Age", command=calculate_age).pack(pady=10)

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Run app
window.mainloop()