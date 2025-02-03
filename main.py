import tkinter as tk
from search_flights import search_flights_window
from book_tickets import book_tickets_window
from boarding_pass import boarding_pass_window

# Main window
root = tk.Tk()
root.title("Airline Booking System")
root.geometry("400x300")
root.configure(bg="light blue")

tk.Label(root, text="Airline Booking System", fg="black", bg="light gray", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(root, text="Search Flights", command=lambda: search_flights_window(root)).pack(pady=5)
tk.Button(root, text="Book Tickets", command=lambda: book_tickets_window(root)).pack(pady=5)
tk.Button(root, text="Generate Boarding Pass", command=lambda: boarding_pass_window(root)).pack(pady=5)

root.mainloop()
