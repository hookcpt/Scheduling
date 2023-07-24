#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:58:03 2023

@author: hue
"""

import random 
import string
from datetime import datetime, timedelta
import csv

'''MOVIES'''

# Generate Movie data
titles = ['Star Wars: The Force Unleashed', 'Star Trek: Rise of the Borg', 'Utopia: Beyond the Horizon', 
          'Avatar: The Next Generation', 'Lord of the Rings: The Age of Elves', 
          'The Avengers: Endgame', 'Jurassic World: Fallen Kingdom', 'Black Panther', 'Incredibles 2', 'Bohemian Rhapsody']

movies = []

# Set price based on title
price_dict = {'Star Wars: The Force Unleashed': 15, 'Star Trek: Rise of the Borg': 15, 'Utopia: Beyond the Horizon': 10, 
              'Avatar: The Next Generation': 10, 'Lord of the Rings: The Age of Elves': 15, 
              'The Avengers: Endgame': 10, 'Jurassic World: Fallen Kingdom': 10, 'Black Panther': 10, 
              'Incredibles 2': 10, 'Bohemian Rhapsody': 10}

# Set initial release date
release_date = datetime(2023, 4, 15)

for title in titles:
    # Generate movie ID
    movie_id = random.randint(1000, 9999)
    
    # Set price based on title
    price = price_dict[title]
    
    # Generate show times
    show_times = []
    days_since_release = 0
    while days_since_release <= 70:
        if days_since_release == 0:
            show_times.append(datetime.strptime('12:00 PM', '%I:%M %p').strftime('%I:%M %p'))
            show_times.append(datetime.strptime('3:00 PM', '%I:%M %p').strftime('%I:%M %p'))
            show_times.append(datetime.strptime('6:00 PM', '%I:%M %p').strftime('%I:%M %p'))
        elif days_since_release % 3 == 0:
            show_times.append(datetime.strptime('12:00 PM', '%I:%M %p').strftime('%I:%M %p'))
        elif days_since_release % 3 == 1:
            show_times.append(datetime.strptime('3:00 PM', '%I:%M %p').strftime('%I:%M %p'))
        else:
            show_times.append(datetime.strptime('6:00 PM', '%I:%M %p').strftime('%I:%M %p'))
        days_since_release += 1
    
    # Add movie data to list
    movie_data = [movie_id, title, price, release_date.strftime("%Y-%m-%d"), show_times]
    movies.append(movie_data)
    
    # Increment release date
    release_date += timedelta(days=random.randint(5, 10))

# Write movie data to CSV
with open('movies.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Movie ID', 'Title', 'Price', 'Release Date', 'Show Times'])
    writer.writerows(movies)

'''THEATHER CHARACTERISTICS'''

# Read movie names from movies.csv
with open('movies.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    movie_names = [row[1] for row in reader]

# Create theater characteristics file with movie names and available seats
with open('theater_characteristics.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Available Movies', 'Available Seats'])
    for movie in movie_names:
        writer.writerow([movie, 150])





''' 

    # Choose a random number of bookings for the showtime
    num_bookings = random.randint(0, Seats)

    # Get the current booking count for this movie ID
    booking_count = booking_counts.get(Movie ID, 0)

    # Write headers to the file if it's empty
    if index == 0:
        with open('Transactions.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Transaction ID', 'Customer Name', 'Movie ID', 'Movie Title', 'Price', 'Scheduling Date', 'Show Time'])

for i in range(200):
    # Generate a random transaction ID
    transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    # Choose a random customer name
    fake = Faker()

    # Generate a random first name
    first_name = fake.first_name()

    # Generate a random last name
    last_name = fake.last_name()
    
    customer_name = f"{first_name} {last_name}"
    
    # Choose a random date from the available dates in the showtimes_df
    date = random.choice(showtimes_df['scheduling date'])

    # Choose a random show time from the available show times for the chosen date
    show_times = showtimes_df.loc[showtimes_df['scheduling date']==date, 'Show Time'].tolist()
    show_time = random.choice(show_times)

    # Extract movie details from the showtimes_df
    movie = showtimes_df.loc[(showtimes_df['scheduling date']==date) & (showtimes_df['Show Time']==show_time)].iloc[0]
    movie_id = movie['Movie ID']
    movie_title = movie['Movie Name']
    movie_price = movie['Price'] 
    
    # Calculate the remaining seats for the chosen show time and date
    seats_remaining = int(movie['Seats'])
    bookings = pd.read_csv('Transactions.csv', parse_dates=['scheduling date'])
    bookings = bookings.loc[(bookings['Movie ID']==movie_id) & (bookings['scheduling date']==date) & (bookings['Show Time']==show_time)]
    seats_booked = bookings.shape[0]
    seats_remaining -= seats_booked

    # Generate a random number of bookings for the chosen show time and date
    num_bookings = random.randint(0, seats_remaining)

    # Write the transactions to the file
    with open('Transactions.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for j in range(num_bookings):
            # Write the transaction to the file
            writer.writerow([transaction_id, customer_name, movie_id, movie_title, movie_price, date.strftime('%Y-%m-%d'), show_time])




showtimes
  days_since_release = 0
  while days_since_release <= 25:
      if days_since_release == 0:
          show_times.append(datetime.strptime('12:00 PM', '%I:%M %p').strftime('%I:%M %p'))
          show_times.append(datetime.strptime('3:00 PM', '%I:%M %p').strftime('%I:%M %p'))
          show_times.append(datetime.strptime('6:00 PM', '%I:%M %p').strftime('%I:%M %p'))
      elif days_since_release % 3 == 0:
          show_times.append(datetime.strptime('12:00 PM', '%I:%M %p').strftime('%I:%M %p'))
      elif days_since_release % 3 == 1:
          show_times.append(datetime.strptime('3:00 PM', '%I:%M %p').strftime('%I:%M %p'))
      else:
          show_times.append(datetime.strptime('6:00 PM', '%I:%M %p').strftime('%I:%M %p'))
      days_since_release += 1




from faker import Faker

import random
import ast

# Read movie data from movies.csv
with open('movies.csv', mode='r') as file:
    reader = csv.DictReader(file)
    movies_data = [row for row in reader]

# Generate bookings using movie data
for i in range(100):
    # Generate a random transaction ID
    transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    # Choose a random customer name
    fake = Faker()

    # Generate a random first name
    first_name = fake.first_name()

    # Generate a random last name
    last_name = fake.last_name()
    
    customer_name = f"{first_name} {last_name}"
    
    # Choose a random movie from movies_data
    movie = random.choice(movies_data)

    # Extract movie details
    movie_id = movie['Movie ID']
    movie_title = movie['Title']
    movie_price = movie['Price'] 
    release_date = datetime.strptime(movie['Release Date'], '%Y-%m-%d').date()
    show_times = ast.literal_eval(movie['Show Times'])

    # Choose a random date from release_date to release_date + 21 days
    date = release_date + timedelta(days=random.randint(0, 21))

    # Choose a random show time
    show_time = random.choice(show_times)

    # Write the transaction to the file
    with open('Transactions.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([transaction_id, customer_name, movie_id, movie_title, movie_price, date.strftime('%Y-%m-%d'), show_time])
        f.write(f'{transaction_id},{customer_name},{date},{show_time},{movie_id}\n')

Bookingsold 


# generate a list of movie ids
movies = ['M001', 'M002', 'M003', 'M004', 'M005']

# generate a list of customer names
names = ['John', 'Emily', 'Alex', 'Emma', 'Liam', 'Olivia', 'Noah', 'Ava']

# generate a list of dates
dates = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-05']

# generate a list of show times
show_times = ['10:00', '13:00', '16:00', '19:00', '22:00']

# generate 100 random transactions
for i in range(100):
    # generate a random transaction id
    transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    # choose a random customer name
    customer_name = random.choice(names)

    # choose a random movie id
    movie_id = random.choice(movies)

    # choose a random date
    date = random.choice(dates)

    # choose a random show time
    show_time = random.choice(show_times)

    # write the transaction to the file
    with open('Transactions.csv', 'a') as f:
        f.write(f'{transaction_id},{customer_name},{date},{show_time},{movie_id}\n')














Movies
# generate a list of movie ids
movieID = ['M001', 'M002', 'M003', 'M004', 'M005']

# generate a list of Movie Titles

title = ['Star Wars', 'Star trek', 'Utopia', 'Avatar', 'Lord of the rings']

Price = [10, 15]

#Generate a list of Releasedates
# Get the current date
Release_Date = datetime.now()

# Create a list to hold the thirty days from today
dates = []

# Loop over the range of seven days and add each day to the list
for i in range(30):
    date = current_date + timedelta(days=i)
    dates.append(date.strftime('%Y-%m-%d'))

# Print the list of dates
print(dates, show_times)

import re

# ...

show_times = re.split('[,; ]+', row['Show times'])
show_times = [datetime.strptime(t.strip(), '%I:%M %p') for t in show_times]



# generate a list of show times
show_times = ['10:00', '13:00', '16:00', '19:00', '22:00']

# write the transaction to the file
with open('Movies.csv', 'a') as f:
    f.write(f'{transaction_id},{customer_name},{date},{show_time},{movie_id}\n')



# generate a list of dates  Loop over the range of 30 days and add each day to the list
Releasedates = [
for i in range(30):
    date = current_date + timedelta(days=i)
    dates.append(date.strftime('%Y-%m-%d'))

# Print the list of dates
print(dates, show_times)]

# generate 100 random transactions
for i in range(100):
    # generate a random transaction id
    transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    # choose a random customer name
    customer_name = random.choice(names)

    # choose a random movie id
    movie_id = random.choice(movies)

    # choose a random date
    date = random.choice(dates)

    # choose a random show time
    show_time = random.choice(show_times)

    # write the transaction to the file
    with open('bookings.csv', 'a') as f:
        f.write(f'{transaction_id},{customer_name},{date},{show_time},{movie_id}\n')
        
'''