#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 00:12:06 2023

@author: hue
"""
import csv
import ast
from datetime import datetime, timedelta
import pandas as pd
import datetime as dt

movies_df = pd.read_csv('movies.csv')
theater_df = pd.read_csv('theater_characteristics.csv')
movies_df['available seats'] = theater_df['Available Seats']

# define today's date
today = dt.date.today()

# create a range of dates for the next 8 weeks, with a frequency of 1 day
date_range = pd.date_range(start=today, end=today+dt.timedelta(weeks=8), freq='D')
daterange_df= pd.DataFrame({'Scheduling Date': date_range})
daterange_df ['MovieID']= movies_df ['Movie ID']

# create an empty DataFrame to store the showtimes schedule
showtimes_df = pd.DataFrame(columns=['Movie Name', 'Movie ID', 'Price', 'Seats', 'Scheduling Date', 'Show Time'])

# loop over each date in the date range
for scheduling_date in date_range:
    
    # create a list to store the available showtimes for the current date
    available_showtimes = []
    
    # loop over each movie in the movies DataFrame
    for index, row in movies_df.iterrows():
        
        # check if the movie has already been scheduled for the current date
        if len(showtimes_df.loc[(showtimes_df['Scheduling Date'] == scheduling_date) & (showtimes_df['Movie ID'] == row['Movie ID'])]) > 0:
            continue
        
        # check if the movie has been released more than 56 days ago
        # check if the movie has been released more than 56 days ago
        release_date = datetime.strptime(row['Release Date'], '%Y-%m-%d').date()
        if (scheduling_date.date() - release_date).days > 56:
            continue
        
        # unpack the showtimes for the current movie
        showtimes = ast.literal_eval(row['Show Times'])
        
        # loop over each showtime for the current movie
        for showtime in showtimes:
            # check if the showtime has already been scheduled for the current date
            if (scheduling_date, showtime) in available_showtimes:
                continue
            
            # add the showtime to the list of available showtimes for the current date
            available_showtimes.append((scheduling_date, showtime))
            
            # add the showtime to the showtimes DataFrame
            showtimes_df = showtimes_df.append({
                'Movie Name': row['Title'],
                'Movie ID': row['Movie ID'],
                'Price': row['Price'],
                'Seats': row['available seats'],
                'Scheduling Date': scheduling_date,
                'Show Time': datetime.strptime(showtime, '%I:%M %p').strftime('%I:%M %p')
            }, ignore_index=True)
            
            # break out of the loop if a showtime has been scheduled for the current movie
            break

print ('Schedule')
print (showtimes_df)


# Write headers to the file
with open('Schedule.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Movie Name', 'Movie ID', 'Price', 'Seats', 'Scheduling Date', 'Show Time'])

# Write data to the file
with open('Schedule.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for index, row in showtimes_df.iterrows():
        writer.writerow([row['Movie Name'], row['Movie ID'], row['Price'], row['Seats'], row['Scheduling Date'], row['Show Time']])




'''

____________________________
import csv
import ast
from datetime import datetime, timedelta
import pandas as pd
import datetime as dt

import pandas as pd
import datetime as dt

movies_df = pd.read_csv('movies.csv')
theater_df = pd.read_csv('theater_characteristics.csv')
movies_df['available seats'] = theater_df['Available Seats']

# define today's date
today = dt.date.today()
print(today)

# create a range of dates for the next 20 weeks, with a frequency of 1 day
date_range = pd.date_range(start=today, end=today+dt.timedelta(weeks=20), freq='D')
daterange_df= pd.DataFrame({'Scheduling Date': date_range})
daterange_df ['MovieID']= movies_df ['Movie ID']

print (daterange_df)


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# create an empty DataFrame to store the unpacked showtimes
showtimes_df = pd.DataFrame(columns=['Movie Name', 'Movie ID', 'Price', 'Seats', 'Scheduling Date', 'Show Time'])

# iterate over each row in the movies DataFrame
for index, row in movies_df.iterrows():
    # get the showtimes for the current movie
    showtimes = ast.literal_eval(row['Show Times'])
    # iterate over each showtime and add a row to the showtimes DataFrame
    for showtime in showtimes:
        showtimes_df = showtimes_df.append({
            'Movie Name': row['Title'],
            'Movie ID': row['Movie ID'],
            'Price': row['Price'],
            'Seats': row['available seats'],
            'Scheduling Date': row['Release Date'], 
            'Show Time': datetime.strptime(showtime, '%I:%M %p').strftime('%I:%M %p')
        }, ignore_index=True)

print ('Schedule') 
print (showtimes_df)

import csv

# Write headers to the file
with open('Schedule.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Movie Name', 'Movie ID', 'Price', 'Seats', 'Scheduling Date', 'Show Time'])

# Write data to the file
with open('Schedule.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for index, row in showtimes_df.iterrows():
        writer.writerow([row['Movie Name'], row['Movie ID'], row['Price'], row['Seats'], row['Scheduling Date'], row['Show Time']])




____________________________________________________________________________-

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# create an empty DataFrame to store the unpacked showtimes
showtimes_df = pd.DataFrame(columns=['scheduling date', 'Show Time'])

# iterate over each row in the movies DataFrame
for index, row in movies_df.iterrows():
    # get the showtimes for the current movie
    showtimes = ast.literal_eval(row['Show Times'])
    # iterate over each showtime and add a row to the showtimes DataFrame
    for showtime in showtimes:
        showtimes_df = showtimes_df.append({
            'Movie Name': row['Title'],
            'Movie ID': row['Movie ID'],
            'Price': row['Price'],
            'Seats': row['available seats'],
            'scheduling date': row['Release Date'], 
            'Show Time': showtime
        }, ignore_index=True)

print ('scaleton Schedule') 
print (showtimes_df)


daterange_df['show time']= showtimes_df['Show Time']

print (daterange_df)


# create an empty DataFrame to store the unpacked showtimes
showtimes_df = pd.DataFrame(columns=['scheduling date', 'Show Time'])

# iterate over each row in the movies DataFrame
for index, row in movies_df.iterrows():
    # get the showtimes for the current movie
    showtimes = ast.literal_eval(row['Show Times'])
    # iterate over each showtime and add a row to the showtimes DataFrame
    for showtime in showtimes:
        showtimes_df = showtimes_df.append({'scheduling date': row['Release Date'], 'Show Time': showtime}, ignore_index=True)

# create binary indicators for each unique show time
showtimes_dummies = pd.get_dummies(showtimes_df['Show Time'])

# concatenate daterange_df and showtimes_dummies along columns axis
merged_df = pd.concat([daterange_df.set_index('scheduling date'), showtimes_dummies], axis=1, join='outer')

print(merged_df)

print (showtimes_df)



# reset index of daterange_df
daterange_df = daterange_df.reset_index(drop=True)

# reset index of showtimes_df
showtimes_df = showtimes_df.reset_index(drop=True)

# concatenate the two dataframes
merged_df = pd.concat([daterange_df, showtimes_df], axis=1, join='outer')


# print the merged DataFrame with the unpacked showtimes




# drop duplicates in the showtimes_df DataFrame
showtimes_df = showtimes_df.drop_duplicates()


# merge the daterange_df and showtimes_df DataFrames
#merged_df = pd.merge(daterange_df, showtimes_df, on='scheduling date', how='outer')

# merge the daterange DataFrame with the unpacked showtimes DataFrame
merged_df = pd.concat([daterange_df.set_index('scheduling date'), showtimes_df.set_index('Show Time')], axis=1, join='outer')

#showtimes_df['scheduling date'] = pd.to_datetime(showtimes_df['date_str'])

# sort the merged DataFrame by date and time
merged_df.sort_values(['scheduling date', 'Show Time'], inplace=True)

# reset the index of the merged DataFrame
merged_df.reset_index(drop=True, inplace=True)


# merge the two DataFrames on the common 'theater_id' column
merged_df = pd.merge(movies_df, theater_df, on='Title')

# define today's date
today = dt.date.today()

# create a range of dates for the next 10 weeks, with a frequency of 1 day
date_range = pd.date_range(start=today, end=today+dt.timedelta(weeks=10), freq='D')


daterange_df= pd.DataFrame({'scheduling date': date_range})
daterange_df ['Show Times'] = movies_df['Show Times']

df = pd.DataFrame('Show Times')

# define a function to convert the string representation of the list into a list
def convert_to_list(s):
    s = s.strip("[']")
    return s.split("', '")

# apply the function to the 'showtimes' column and convert the result to a DataFrame
showtimes_df = df['Show Times'].apply(convert_to_list).apply(pd.Series)

# concatenate the new DataFrame with the original DataFrame
merged_df = pd.concat([df, showtimes_df], axis=1)

# drop the original 'showtimes' column
merged_df.drop('Show Times', axis=1, inplace=True)

# print the merged DataFrame with the unpacked showtimes
print(merged_df)


print (daterange_df)





def schedule_movies():
    # Read movie data from CSV file
    movies = []
    all_show_times = set()
    with open('movies.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extract list of show times from string representation in CSV file
            show_times = ast.literal_eval(row['Show Times'])
            # Convert string representation of show times to a datetime.time object
            show_times = [datetime.strptime(t, '%I:%M %p').time() for t in show_times]
            # Convert string representation of release date to a datetime.date object
            release_date = datetime.strptime(row['Release Date'], '%Y-%m-%d').date()
            # Add movie data to list of movies
            movies.append({
                'id': int(row['Movie ID']),
                'title': row['Title'],
                'price': int(row['Price']),
                'release_date': release_date,
                'show_times': show_times
            })
            # Add show times for this movie to set of all show times
            all_show_times.update(show_times)

    # Sort movies by release date, in ascending order
    movies = sorted(movies, key=lambda x: x['release_date'])

    # Determine start and end dates for scheduling
    start_date = datetime.today().date()
    end_date = start_date + timedelta(weeks=8)

    # Initialize schedule
    schedule = []
    current_date = start_date
    while current_date <= end_date:
        schedule.append({
            'date': current_date,
            'movies': [],
            'available_show_times': all_show_times.copy()
        })
        current_date += timedelta(days=1)

    # Schedule movies
    for movie in movies:
        if movie['release_date'] > end_date:
            continue
        
        current_date = movie['release_date']
        #determine available showtimes
        
        available_show_times = {show_time: True for show_time in movie['show_times']}
        
        while current_date <= end_date and available_show_times:
        
            if current_date < movie['release_date'] + timedelta(days=0):
                show_time = next((show_time for show_time in movie['show_times'] if available_show_times[show_time]), None)
                if show_time is None:
                    break
                available_show_times[show_time] = False
            
            else:
                show_time = next((show_time for show_time in movie['show_times'] if available_show_times[show_time]), None)
                if show_time is None:
                    show_time = movie['show_times'][0]
                available_show_times[show_time] = False
            schedule_date = next((item for item in schedule if item['date'] == current_date), None)
            if schedule_date is not None:
                if show_time in schedule_date['available_show_times']:
                    schedule_date['movies'].append({
                        'id': movie['id'],
                        'title': movie['title'],
                        'price': movie['price'],
                        'show_time': show_time
                    })
                    schedule_date['available_show_times'].remove(show_time)
            current_date += timedelta(days=2)

    # Return schedule
  
def print_schedule(schedule):
    print("{:<12} {:<30} {:<10} {:<10}".format("Date", "Title", "Price", "Show Time"))
    for schedule_item in schedule:
        for movie in schedule_item['movies']:
            print("{:<12} {:<30} {:<10} {:<10}".format(schedule_item['date'].strftime('%Y-%m-%d'), movie['title'], movie['price'], movie['show_time'].strftime('%I:%M %p')))

schedule_df = schedule_movies()
print_schedule(schedule_df)


def schedule_movies():
    # Read movie data from CSV file
    movies = []
    all_show_times = set()
    with open('movies.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extract list of show times from string representation in CSV file
            show_times = ast.literal_eval(row['Show Times'])
            # Convert string representation of show times to a datetime.time object
            show_times = [datetime.strptime(t, '%I:%M %p').time() for t in show_times]
            # Convert string representation of release date to a datetime.date object
            release_date = datetime.strptime(row['Release Date'], '%Y-%m-%d').date()
            # Add movie data to list of movies
            movies.append({
                'id': int(row['Movie ID']),
                'title': row['Title'],
                'price': int(row['Price']),
                'release_date': release_date,
                'show_times': show_times
            })
            # Add show times for this movie to set of all show times
            all_show_times.update(show_times)

    # Sort movies by release date, in ascending order
    movies = sorted(movies, key=lambda x: x['release_date'])

    # Determine start and end dates for scheduling
    start_date = datetime.today().date()
    end_date = start_date + timedelta(weeks=8)

    # Initialize schedule
    schedule = []
    current_date = start_date
    while current_date <= end_date:
        schedule.append({
            'date': current_date,
            'movies': [],
            'available_show_times': all_show_times.copy()
        })
        current_date += timedelta(days=1)

    # Schedule movies
    for movie in movies:
        if movie['release_date'] > end_date:
            continue
        
        current_date = movie['release_date']
        #determine available showtimes
        
        available_show_times = {show_time: True for show_time in movie['show_times']}
        
        while current_date <= end_date and available_show_times:
        
            if current_date < movie['release_date'] + timedelta(days=0):
                show_time = next((show_time for show_time in movie['show_times'] if available_show_times[show_time]), None)
                if show_time is None:
                    break
                available_show_times[show_time] = False
            
            else:
                show_time = next((show_time for show_time in movie['show_times'] if available_show_times[show_time]), None)
                if show_time is None:
                    show_time = movie['show_times'][0]
                available_show_times[show_time] = False
            schedule_date = next((item for item in schedule if item['date'] == current_date), None)
            if schedule_date is not None:
                if show_time in schedule_date['available_show_times']:
                    schedule_date['movies'].append({
                        'id': movie['id'],
                        'title': movie['title'],
                        'price': movie['price'],
                        'show_time': show_time
                    })
                    schedule_date['available_show_times'].remove(show_time)
            current_date += timedelta(days=2)

    # Return schedule
  
def print_schedule(schedule):
    print("{:<12} {:<30} {:<10} {:<10}".format("Date", "Title", "Price", "Show Time"))
    for schedule_item in schedule:
        for movie in schedule_item['movies']:
            print("{:<12} {:<30} {:<10} {:<10}".format(schedule_item['date'].strftime('%Y-%m-%d'), movie['title'], movie['price'], movie['show_time'].strftime('%I:%M %p')))

schedule_df = schedule_movies()
print_schedule(schedule_df)
'''
