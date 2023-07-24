#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:30:30 2023

@author: hue
"""
import sys
import pandas as pd
import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
import importlib

# Execute the CountBookings script
exec(open('CountBookings.py').read())

# Import the script as a module
count_bookings_module = importlib.import_module('CountBookings')

class BookingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Booking System")
        self.prev_bookings_df = pd.read_csv('Transactions.csv')
        self.display_schedule_df = pd.read_csv('Full_Schedule.csv')
        self.start_screen()

    def start_screen(self):
        self.master.geometry("300x200")
        welcome_label = tk.Label(self.master, text="Welcome to our booking system", font=("Arial", 20))
        welcome_label.pack(pady=20)
        book_button = tk.Button(self.master, text="Book a ticket", command=self.count_bookings)
        book_button.pack()

    def count_bookings(self):
        count_bookings_module.showtimes_df = self.display_schedule_df  # Update the showtimes_df in the CountBookings module
        self.display_schedule_df = pd.read_csv('Full_Schedule.csv')  # Update the data frame
        self.date_selection()

    def date_selection(self):
        self.master.geometry("300x300")
        for widget in self.master.winfo_children():  # Clearing the window
            widget.destroy()
        label = tk.Label(self.master, text="Please select a date", font=("Arial", 20))
        label.pack(pady=20)

        self.cal = Calendar(self.master, selectmode='day')
        self.cal.pack(pady=20)
        ok_button = tk.Button(self.master, text="OK", command=self.get_date)
        ok_button.pack()

    def get_date(self):
        self.date = self.cal.selection_get()  # Get selected date
        self.count_bookings()  # Call the count_bookings function
        self.movie_selection()  # Continue to the movie selection page

    def movie_selection(self):
        for widget in self.master.winfo_children():  # Clearing the window
            widget.destroy()
    
        self.master.geometry("800x500")  # You might want to adjust this for better layout
        label = tk.Label(self.master, text="Please select a movie and showtime", font=("Arial", 20))
        label.grid(row=0, column=0, columnspan=4, pady=20)
    
        # Filter the DataFrame for the selected date
        available_movies_df = self.display_schedule_df[self.display_schedule_df['Scheduling Date'] == self.date.strftime('%Y-%m-%d')]
    
        # Create a dictionary of listboxes with their widths
        listboxes = {'movies': {'box': None, 'width': 50}, 'showtimes': {'box': None, 'width': 10},
                     'seats': {'box': None, 'width': 10}, 'prices': {'box': None, 'width': 10}}
    
        headers = {'movies': 'Movie (ID)', 'showtimes': 'Showtime', 'seats': 'Seats', 'prices': 'Price'}
    
        # Initialize and place the listboxes
        for idx, (key, value) in enumerate(listboxes.items()):
            tk.Label(self.master, text=headers[key], font=("Arial", 16)).grid(row=1, column=idx, padx=10)
            listboxes[key]['box'] = tk.Listbox(self.master, width=value['width'])
            listboxes[key]['box'].grid(row=2, column=idx, padx=10)
    
        # Populate the listboxes
        for _, row in available_movies_df.iterrows():
            listboxes['movies']['box'].insert(tk.END, f"{row['Movie Name']} (ID: {row['Movie ID']})")
            listboxes['showtimes']['box'].insert(tk.END, row['Show Time'])
            listboxes['seats']['box'].insert(tk.END, row['Available Seats'])
            listboxes['prices']['box'].insert(tk.END, row['Price'])
    
        # Store listboxes in self for later access
        self.movies_listbox = listboxes['movies']['box']
        self.showtimes_listbox = listboxes['showtimes']['box']
        self.seats_listbox = listboxes['seats']['box']
        self.prices_listbox = listboxes['prices']['box']
    
        ok_button = tk.Button(self.master, text="OK", command=self.get_movie)
        ok_button.grid(row=3, column=0, columnspan=4, pady=20)


    def get_movie(self):
        try:
            movie_index = self.movies_listbox.curselection()[0]  # Get selected movie
        except IndexError:
            messagebox.showerror("Error", "Please select a movie")
            return
    
        self.movie = self.movies_listbox.get(movie_index)
        self.showtime = self.showtimes_listbox.get(movie_index)
        self.available_seats = self.seats_listbox.get(movie_index)
        self.price = self.prices_listbox.get(movie_index)
    
        self.ticket_selection()  # Continue to the ticket selection page
    
    def ticket_selection(self):
        for widget in self.master.winfo_children():  # Clearing the window
            widget.destroy()
        self.master.geometry("800x500")
        label = tk.Label(self.master, text="Please select the number of tickets", font=("Arial", 20))
        label.pack(pady=20)
        self.tickets_spinbox = tk.Spinbox(self.master, from_=1, to=int(self.available_seats))
        self.tickets_spinbox.pack(pady=20)
        self.tickets_spinbox.update()  # Force update
    
        ok_button = tk.Button(self.master, text="OK", command=self.get_tickets)
        ok_button.pack()

  
    def get_tickets(self):
        self.tickets = int(self.tickets_spinbox.get())  # Get selected number of tickets
        self.customer_information()
        
    def customer_information(self):
        for widget in self.master.winfo_children():  # Clearing the window
            widget.destroy()
    
        self.master.geometry("800x500")
    
        label = tk.Label(self.master, text="Please enter the customer's name", font=("Arial", 20))
        label.pack(pady=20)
    
        # Create one entry field for each ticket
        self.customer_entries = []
        for i in range(self.tickets):
            entry = tk.Entry(self.master)
            entry.pack(pady=10)
            entry.update()  # Force update
            self.customer_entries.append(entry)
    
        ok_button = tk.Button(self.master, text="Purchase tickets", command=self.purchase_tickets)
        ok_button.pack()
    
        back_button = tk.Button(self.master, text="Back", command=self.ticket_selection)  # This will go back to ticket selection
        back_button.pack()

    def purchase_tickets(self):
        # Split movie info string to get the movie name and ID
        movie_name, movie_id = self.movie.split(" (ID: ")
        movie_id = movie_id.rstrip(")")
    
        for entry in self.customer_entries:
            customer_name = entry.get()
            # Generate a unique transaction ID
            transaction_id = len(self.prev_bookings_df) + 1
            # Create a new row
            new_row = {
                "Transaction ID": transaction_id,
                "Customer Name": customer_name,
                "Movie ID": movie_id,
                "Movie Title": movie_name,
                "Price": self.price,
                "Scheduling Date": self.date.strftime('%Y-%m-%d'),
                "Show Time": self.showtime
            }
            # Append the new row to the dataframe
            self.prev_bookings_df = self.prev_bookings_df.append(new_row, ignore_index=True)
    
        # Write the updated dataframe to the file
        self.prev_bookings_df.to_csv('Transactions.csv', index=False)
    
        # Display success messages
        messagebox.showinfo("Payment", "Imagine payment process")
        messagebox.showinfo("Success", "Success! Thank you for booking our Theatre")
    
        # Clear the customer information window
        for widget in self.master.winfo_children():
            widget.destroy()
    
        # Add buttons for closing the program and booking another movie
        close_button = tk.Button(self.master, text="Close the Program", command=self.close_program)
        close_button.pack()
    
        book_another_button = tk.Button(self.master, text="Book Another Movie", command=self.date_selection)
        book_another_button.pack()

    def close_program(self):
        sys.exit(0)
            
root = tk.Tk()
app = BookingSystem(root)
root.mainloop()
