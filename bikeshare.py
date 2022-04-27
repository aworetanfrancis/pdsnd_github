import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # gets user input for city (chicago, new york city, washington).
    city = input("Mind to see bikeshare\'s data for Chicago,  New York City, or Washington? ").lower()
    while city not in (CITY_DATA.keys()):
        print('Invalid city name!!!, inputs all lowercaps')
        city = input("Mind to see bikeshare\ 's data for Chicago,  New York, or Washington? ").lower()
  
    # gets user input for filter type (month, day or both).
    filter = input('Mind to filter the data by month, day, both, or none? ').lower()
    while filter not in (['month', 'day', 'both', 'none']):
        print('You provided a wrong filter !')
        filter = input('Mind to filter the data by month, day, both, or none? ').lower()
        
   # gets user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may','june']
    if filter == 'month' or filter == 'both':
        month = input('Select month - January, February, March, April, May, or June? ').lower()
        while month not in months:
            print('invalid month !')
            month = input('Select month - January, February, March, April, May, or June? ').lower()
    else:
        month = 'all'
            
    # gets user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if filter == 'day' or filter == 'both':
        day = input('select day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').title()
        while day not in days:
            print('invalid day!, capitalize first character')
            day = input('select day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').title()
    else:
        day = 'all'
 
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # loads  CITY_DATA file into dataframe

    df = pd.read_csv(CITY_DATA[city])

    # converts the Start_Time column to date_Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extracts month and day of week from Start_Time to create new coumns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    #filters by month if applicable(USINF IF STATEMENT)
    if month != 'all':
        #use the index of the month list to get corresponding list
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        #filter by monthS to create a new dataframe[ASSIGNMENT OPERATION)
        df = df[df['month'] == month]
    #filter by day of week if applicable(USINF IF STATEMENT)
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displays the most common month
    month = df['month'].mode()[0]
    print(f'Most common month(1 = January,...,6 = June): {month}')

    # displays the most common day of week

    day = df['day_of_week'].mode()[0]
    print(f'Most common day of week is:{day}')

    # displays the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f'Most common start hour is:{common_hour}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # displays most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'The most common start station is:{common_start_station}')
    
    # displays most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'The most common end station is:{common_end_station}')
    
    # displays most frequent combination of start station and end station trip
    common_trip = df['Start Station'] + ' to ' + df['End Station']
    print(f'The most popular trip is: from {common_trip.mode()[0]}')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    
    """Displays statistics on the total and average trip duration."""
    from datetime import timedelta as td
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displays total travel time
    total_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days = total_travel_duration.days
    hours = total_travel_duration.seconds // (60*60)
    minutes = total_travel_duration.seconds % (60*60) // 60
    seconds = total_travel_duration.seconds % (60*60) % 60
    print(f'the total travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds')
    

    # displays mean travel time
    
    average_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days = average_travel_duration.days
    hours = average_travel_duration.seconds // (60*60)
    minutes = average_travel_duration.seconds % (60*60) // 60
    seconds = average_travel_duration.seconds % (60*60) % 60
    print(f'Average travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds')
    
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displays counts of user types
    print(df['User Type'].value_counts())
    print('\n\n')


    # Displays counts of gender
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())
        print('\n\n')
        
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in(df.columns):
        year = df['Birth Year'].fillna(0).astype('int64')
        print(f'The Earliest birth year is: {year.min()}\nMost recent is: {year.max()}\nMost common birth year is: {year.mode()[0]}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Ask the user if he wants to display the raw data and print 5 rows at time"""
    raw = input('\nwould you like to display raw data?\n')
    if raw.lower() == "yes":
        counter = 0
        while True:
            print(df.iloc[counter:counter+5])
            counter += 5
            ask = input('next 5 raws?')
            if ask.lower() != 'yes':
                break

 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
