#!/usr/bin/env python
# coding: utf-8

# In[10]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
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
    # TO DO: get user input for city ['chicago','new york city','washington']:. HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input("Please enter city name :")).lower()
        if city not in ['chicago','new york city','washington']:
            print('please enter a vaild city name (chicago or new york city or washington)')
        else:
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month = str(input("Please enter month name : ")).lower()    
        if month not in['all','january','february','march','april','may','june']:
            print('please enter a vaild month name')
        else:
            break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = str(input("Please enter day name: ")).lower()
        if day not in['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']:
            print('please enter a vaild day name')
        else:
            break
    
            
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def vi_data(df):
    
    start_loc = 0
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()

    while True :
        if view_data == "no" :
            break 
        print(df.iloc[0:5])
        view_display = input("Do you wish to continue?: ").lower()
        start_loc += 5

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour , month, day
    popular_month = df['month'].mode()[0]
    popular_day = df['day_of_week'].mode()[0]
    popular_hour = df['hour'].mode()[0]

    
    # TO DO: display the most common month
    print('Most Popular Start month:', popular_month)


    # TO DO: display the most common day of week
    print('Most Popular Start day of week:', popular_day)


    # TO DO: display the most common start hour
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    co_start_station = df['Start Station'].mode()[0]
    co_end_station = df['End Station'].mode()[0]
    
    df['Start - End Station'] =  df['Start Station'] + " " + df['End Station']
    co_comb_station = df['Start - End Station'].mode()[0]
    
    # TO DO: display most commonly used start station
    print('Most Popular start station:', co_start_station)

    # TO DO: display most commonly used end station
    print('Most Popular End station:', co_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    print('most frequent combination of start station and end station:', co_comb_station)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    t_tra_time = df['Trip Duration'].sum()
    print('total travel time is :', t_tra_time)

    # TO DO: display mean travel time
    avg_tra_time = df['Trip Duration'].mean()
    print('average travel time is :', avg_tra_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        ear_year = int(df['Birth Year'].min())
        m_com_year = int(df['Birth Year'].mode()[0])
        m_rec_year = int(df['Birth Year'].max())    

    print('Earliest Year is :',ear_year)
    print('Most Recent Year is :',m_com_year)
    print('Most Common Year is :',m_rec_year)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        vi_data(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




