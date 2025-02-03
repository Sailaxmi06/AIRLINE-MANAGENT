import tkinter as tk
from tkinter import messagebox
from airline_data import FLIGHTS

def book_tickets_window(root):
    book_window = tk.Toplevel(root)
    book_window.title("Book Tickets")
    book_window.geometry("500x300")
    book_window.configure(bg="sky blue")
    
    tk.Label(book_window, text="Enter Flight Number:").pack()
    flight_entry = tk.Entry(book_window)
    flight_entry.pack()

    tk.Label(book_window, text="Passenger Name:").pack()
    name_entry = tk.Entry(book_window)
    name_entry.pack()

    def book_ticket():
        flight_no = flight_entry.get()
        passenger_name = name_entry.get()

        if not flight_no or not passenger_name:
            messagebox.showerror("Error", "All fields are required!")
            return

        flight = next((f for f in FLIGHTS if f["flight_no"] == flight_no), None)

        if flight:
            messagebox.showinfo("Success", f"Ticket booked for {passenger_name} on {flight_no}")
            with open("ticket.txt", "w") as file:
                file.write(f"Passenger: {passenger_name}\nFlight: {flight_no}\nFrom: {flight['from']}\nTo: {flight['to']}\nDeparture: {flight['departure']}\nPrice: ${flight['price']}")
        else:
            messagebox.showerror("Error", "Flight not found!")

    tk.Button(book_window, text="Book Ticket", command=book_ticket).pack(pady=5)
