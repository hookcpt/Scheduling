#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 16:39:32 2023

@author: hue
"""

from Scheduling import showtimes_df
import pandas as pd

# Read in the previous bookings data
prev_bookings_df = pd.read_csv('Transactions.csv')

# Convert the Scheduling Date column to a datetime data type
prev_bookings_df['Scheduling Date'] = pd.to_datetime(prev_bookings_df['Scheduling Date'])

# Group the data by the dates in the column Scheduling Date
date_groups = prev_bookings_df.groupby(prev_bookings_df['Scheduling Date'].dt.date)

# Create an empty list to store the values
Bookings_list = []

# Loop through each date group
for date, date_group in date_groups:
    # Group the date group by the time in the Show Time column
    time_groups = date_group.groupby('Show Time')

    # Loop through each time group
    for time, time_group in time_groups:
        # Count the number of bookings in the time group
        num_bookings = len(time_group)

        # Get the movie ID and title of the time group
        movie_id = time_group['Movie ID'].iloc[0]
        movie_title = time_group['Movie Title'].iloc[0]

        # Get the Scheduling Date of the date group
        scheduling_date = date_group['Scheduling Date'].iloc[0]

        # Add the values to the list
        Bookings_list.append([scheduling_date, time, movie_id, num_bookings])


# Create a DataFrame from the list of values
bookings_df = pd.DataFrame(Bookings_list, columns=['Scheduling Date', 'Show Time', 'Movie ID', 'Num Bookings'])

bookings_df['Scheduling Date'] = pd.to_datetime(bookings_df['Scheduling Date'])

# Merge the bookings_df and showtimes_df dataframes based on the common columns
Display_Schedule_df = pd.merge(showtimes_df, bookings_df, on=['Scheduling Date', 'Show Time', 'Movie ID'])

# Calculate the difference between the Seats and Num Bookings columns for each row
Display_Schedule_df['Available Seats'] = Display_Schedule_df.apply(lambda row: row['Seats'] - row['Num Bookings'], axis=1)

# Save the updated DataFrame to 'Full_Schedule.csv'
Display_Schedule_df.to_csv('Full_Schedule.csv', index=False)

# Print the resulting dataframe
print(Display_Schedule_df)
