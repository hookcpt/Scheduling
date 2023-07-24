#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:37:29 2023

@author: hue
"""
#!/usr/bin/env python3
'''Bookings'''

from faker import Faker
import random
import csv
from datetime import datetime

# Read showtimes data from dataframe
from Scheduling import showtimes_df

# Create a dictionary to store the count of bookings per movie ID
booking_counts = {}

# Generate a list of random customer names
fake = Faker()
customer_names = [fake.name() for i in range(100)]

# Write headers to the file if it's empty
with open('Transactions.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Transaction ID', 'Customer Name', 'Movie ID', 'Movie Title', 'Price', 'Scheduling Date', 'Show Time'])

# Generate bookings using showtimes_df
for index, row in showtimes_df.iterrows():
    # Extract showtime details
    movie_id = row['Movie ID']
    movie_price = row['Price']
    movie_title = row ['Movie Name']
    seats = row['Seats']
    scheduling_date = row['Scheduling Date'].date()
    show_time = datetime.strptime(row['Show Time'], '%I:%M %p').strftime('%I:%M %p')
    
    # Choose a random number of bookings for the showtime
    num_bookings = random.randint(5, seats)

    # Get the current booking count for this movie ID
    booking_count = booking_counts.get(movie_id, 0)

    for i in range(num_bookings):
        # Generate a transaction ID based on the current booking count for this movie ID
        transaction_id = f"{movie_id}_{booking_count+i+1}"

        # Choose a random customer name
        customer_name = random.choice(customer_names)

        # Write the transaction to the file
        with open('Transactions.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([transaction_id, customer_name, movie_id, movie_title, movie_price, scheduling_date.strftime('%Y-%m-%d'), show_time])

        # Update the booking count for this movie ID
        booking_counts[movie_id] = booking_count + num_bookings

'''
from faker import Faker
import random
import csv
from datetime import datetime

# Read showtimes data from dataframe
from Scheduling import showtimes_df

# Create a dictionary to store the count of bookings per movie ID
booking_counts = {}

# Generate a list of random customer names
fake = Faker()
customer_names = [fake.name() for i in range(100)]

# Generate bookings using showtimes_df
for index, row in showtimes_df.iterrows():
    # Extract showtime details
    movie_id = row['Movie ID']
    movie_price = row['Price']
    movie_title = row ['Movie Name']
    seats = row['Seats']
    scheduling_date = datetime.strptime(row['Scheduling Date'], '%Y-%m-%d').date() 
    show_time = datetime.strptime(row['Show Time'], '%I:%M %p').strftime('%I:%M %p')
    
    #'Show Time': datetime.strptime(Show Time, '%I:%M %p').strftime('%I:%M %p')

    # Choose a random number of bookings for the showtime
    num_bookings = random.randint(0, seats)

    # Get the current booking count for this movie ID
    booking_count = booking_counts.get(movie_id, 0)

    # Write headers to the file if it's empty
    if index == 0:
        with open('Transactions.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Transaction ID', 'Customer Name', 'Movie ID', 'Movie Title', 'Price', 'Scheduling Date', 'Show Time'])

    for i in range(num_bookings):
        # Generate a transaction ID based on the current booking count for this movie ID
        transaction_id = f"{movie_id}_{booking_count+i+1}"

        # Choose a random customer name
        customer_name = random.choice(customer_names)

        # Write the transaction to the file
        with open('Transactions.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([transaction_id, customer_name, movie_id, movie_title, movie_price, scheduling_date.strftime('%Y-%m-%d'), show_time])

_______________________________
from faker import Faker
import random
import csv
from datetime import datetime

import pandas as pd

# Read showtimes data from dataframe
from Scheduling import showtimes_df

# Create a dictionary to store the count of bookings per movie ID
booking_counts = {}

# Generate bookings using showtimes_df
for index, row in showtimes_df.iterrows():
    # Extract showtime details
    movie_id = row['Movie ID']
    movie_price = row['Price']
    movie_title = row ['Movie Name']
    seats = row['Seats']
    scheduling_date = datetime.strptime(row['Scheduling Date'], '%Y-%m-%d').date()
    show_time = row['Show Time']

    # Choose a random number of bookings for the showtime
    num_bookings = random.randint(0, seats)

    # Get the current booking count for this movie ID
    booking_count = booking_counts.get(movie_id, 0)

    for i in range(num_bookings):
        # Generate a transaction ID based on the current booking count for this movie ID
        transaction_id = f"{movie_id}-{'{:06}'.format(booking_count + i + 1)}"

        # Choose a random customer name
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        customer_name = f"{first_name} {last_name}"
        
     

        # Write the transaction to the file
        with open('Transactions.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([transaction_id, customer_name, movie_id, movie_title, movie_price, scheduling_date.strftime('%Y-%m-%d'), show_time])
print('done')
#transaction_id,customer_name,movie_id,movie_title,movie_price,date,show_time

   # Update the booking count for this movie ID
  # booking_counts[movie_id] = booking_count + num_bookings



'''













