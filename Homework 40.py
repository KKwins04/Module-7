import tkinter as tk

def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result.config(text=str(cm))

# Window
root = tk.Tk()
root.title("Inches to Centimeter Converter")
root.geometry("300x200")

# Input
tk.Label(root, text="Enter inches:").pack()

entry = tk.Entry(root)
entry.pack()

# Button
tk.Button(root, text="Convert", command=convert).pack()

# Output
result = tk.Label(root, text="")
result.pack()

# Run app
root.mainloop()