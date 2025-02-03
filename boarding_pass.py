import tkinter as tk
from tkinter import messagebox

def boarding_pass_window(root):
    pass_window = tk.Toplevel(root)
    pass_window.title("Generate Boarding Pass")
    pass_window.geometry("500x250")
    pass_window.configure(bg="sky blue")

    
    tk.Label(pass_window, text="Enter Passenger Name:").pack()
    name_entry = tk.Entry(pass_window)
    name_entry.pack()

    result_label = tk.Label(pass_window, text="", justify="left")
    result_label.pack(pady=10)

    def generate_pass():
        name = name_entry.get()
        try:
            with open("ticket.txt", "r") as file:
                ticket_data = file.read()
                if name in ticket_data:
                    result_label.config(text=f"BOARDING PASS\n\n{ticket_data}", font=("Arial", 10, "bold"))
                else:
                    messagebox.showerror("Booking Unavailable", "No booking found for this name.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No ticket found. Please book first!")

    tk.Button(pass_window, text="Generate Boarding Pass", command=generate_pass).pack(pady=5)
