import tkinter as tk
from tkinter import ttk
from airline_data import FLIGHTS

def search_flights_window(root):
    search_window = tk.Toplevel(root)
    search_window.title("Search Flights")
    search_window.geometry("500x400")
    search_window.configure(bg="light blue")

    tk.Label(search_window, text="From:").pack()
    from_entry = tk.Entry(search_window)
    from_entry.pack()

    tk.Label(search_window, text="To:").pack()
    to_entry = tk.Entry(search_window)
    to_entry.pack()

    result_label = tk.Label(search_window, text="", justify="left")
    result_label.pack(pady=10)

    def search():
        from_city = from_entry.get()
        to_city = to_entry.get()
        results = [f for f in FLIGHTS if f["from"] == from_city and f["to"] == to_city]

        if results:
            output = "\n".join([f"Flight: {f['flight_no']} | Departure: {f['departure']} | Price: ${f['price']}" for f in results])
        else:
            output = "No flights found."
        
        result_label.config(text=output)

    tk.Button(search_window, text="Search", command=search).pack(pady=5)
