import tkinter as tk

# Create root window
root = tk.Tk()
root.geometry("500x300")

# Define common widget styles
common_style = {
    "bg": "#2C3E50",  # Background color
    "fg": "white",     # Foreground (text) color
    "font": ("Arial", 14, "bold")
}

# Create widgets using common styles
label = tk.Label(root, text="Hello, Tkinter!", **common_style)
label.pack(pady=10)

button = tk.Button(root, text="Click Me", **common_style)
button.pack(pady=10)

entry = tk.Entry(root, **common_style)
entry.pack(pady=10)

root.mainloop()
