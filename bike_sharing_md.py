# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""
import pandas as pd
import calendar
import pprint
import time
import numpy as np
import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter(indent=3)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'
             }


def choose_city():
    """
    Asks user to specify a city to analyze.

    Returns:
        (str) city - name of the city to analyze
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # get users input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city=input("For which city should your evaluation be based on? \nChicago, \nNew York City \nWashington?\n\n").lower()
        if city == 'chicago':
           print("\nYou have chosen the city of Chicago.\n")
        if city == 'new york city':
           print("\nYou have chosen New York City.\n")
        if city == 'washington':
            print("\nYou have chosen Washington D.C.\n")
        if city not in ('chicago', 'new york city', 'washington'):
            print("\nPlease enter a valid city.")
            continue
        else:
            break

    return city


def choose_month():
    """
    Asks user to specify a month to analyze.

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """

    # get user input for month (all, january, february, ... , june)

    while True:
        month=input("\nWould you like to analyze a specific month or all months together?\nPlease make your selection:\n\nJanuary (01), \nFebruary (02),\nMarch (03), \nApril (04),\nMay (05),\nJune (06),\nall months (all)?\n\n").lower()
        if month=='january' or month=='01':
            print ("\nYou have selected the month of January.\n")
            return 'january'
        elif month=='february' or month=='02':
            print ("\nYou have selected the month of February.\n")
            return 'february'
        elif month=='march' or month=='03':
            print ("\nYou have selected the month of March.\n")
            return 'march'
        elif month=='april' or month=='04':
            print ("\nYou have selected the month of April.\n")
            return 'april'
        elif month=='may' or month=='05':
            print ("\nYou have selected the month of May.\n")
            return 'may'
        elif month=='june' or month=='06':
            print ("\nYou have selected the month of June.\n")
            return 'june'
        if month not in ('01', '02', '03', '04', '05', '06', 'january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("\n Please enter a valid value.")
            continue
        else:
            break

    return month


def choose_day():
    """
    Asks user to specify a day to analyze.

    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day=input("\nWould you like to analyze a specific day of the week?\nPlease make your selection: \n\nMonday (mon), \nTuesday (tue),\nWednesday (wed), \nThursday (thu),\nFriday (fri),\nSaturday (sat),\nSunday (sun),\nall days of the week (all)?\n\n").lower()
        if day=='monday' or day=='mon':
            print ("\nYou have chosen Monday. Please find the statistics for your selection below.\n")
            return 'monday'
        elif day=='tuesday' or day=='tue':
            print ("\nYou have chosen Tuesday. Please find the statistics for your selection below.\n")
            return 'tuesday'
        elif day=='wednesday' or day=='wed':
            print ("\nYou have chosen Wednesday. Please find the statistics for your selection below.")
            return 'wednesday'
        elif day=='thursday' or day=='thu':
            print ("\nYou have chosen Thursday. Please find the statistics for your selection below.\n")
            return 'thursday'
        elif day=='friday' or day=='fri':
            print ("\nYou have chosen Friday. Please find the statistics for your selection below.\n")
            return 'friday'
        elif day=='saturday' or day=='sat':
            print ("\nYou have chosen Saturday. Please find the statistics for your selection below.\n")
            return 'saturday'
        elif day=='sunday' or day=='sun':
            print ("\nYou have chosen Sunday. Please find the statistics for your selection below.\n")
            return 'sunday'
        if day not in ('mon','tue','wed','thu','fri','sat','sun','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'all'):
            print("\n Please enter a valid value.")
            continue
        else:
            break

    return day

    print('_'*50)


def load_choice(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # loading the data from CSV into dataframe

    df = pd.read_csv(CITY_DATA[city])

    # converting timestamp (column 'Start Time') into datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # getting the name of the weekday out of the timestamp

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # getting the month out of the timestamp

    df['month'] = df['Start Time'].dt.month

    # set the filter to month as chosen
        # create the number of the month by index of the list
        # build a new data frame

    if month != 'all':
        months = ['buffer', 'january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
        df = df[df['month'] == month]

    # set the filter to weekday as chosen
        # build a new data frame

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n' + '_'*70 +'\n')
    print('\nCalculating the most frequent times of travel:...\n')
    start_time = time.time()

    # display the most common month
        # Group by month and count the values
        # sort the values ascending and print the highest reslut (last position)

    month_group = df.groupby('month')['Start Time'].count()
    print("Most common month (number of starts):\n\n" + calendar.month_name[int(month_group.sort_values(ascending = True).index[-1])])
    print('\n\nPlease see below mentioned charts for your selection:\n')

    ax=df.groupby('month')['Start Time'].nunique().plot(kind='bar', stacked=True, colormap='Blues_r')
    ax.set_title('Number of starts in selected month(s)')
    ax.set_xlabel('Month')
    ax.set_ylabel('Starts')
    plt.show()

    ax=df.groupby('month')['Trip Duration'].nunique().plot(kind='bar', stacked=True, colormap='Blues_r')
    ax.set_title('Trip duration in selected month(s)')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total trip duration')
    plt.show()

    most_common_weekday = df['day_of_week'].mode()[0]
    print('\n\nMost common day of the week:\n')
    print(most_common_weekday)

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('\n\nMost common hour:\n')
    print(most_common_hour)

    print('\n(This calculation took:', '{:0,.2f}'.format((time.time() - start_time)), 'seconds.)\n')
    print('_'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip:...\n')
    start_time = time.time()

    # display most commonly used start station

    most_common_start_station=df['Start Station'].value_counts()[df['Start Station'].value_counts() == df['Start Station'].value_counts().max()]
    print('Most common start station:\n\n', most_common_start_station)

    # display most commonly used end station
    most_common_end_station=df['End Station'].value_counts()[df['End Station'].value_counts() == df['End Station'].value_counts().max()]
    print('\n\nMost common end station:\n\n', most_common_end_station)

    # display most frequent combination of start station and end station

    most_common_combination=df.groupby(['Start Station', 'End Station']).size().nlargest(3).sort_values(ascending=False)
    print('\n\nMost common three combinations of start station and end station:\n\n', most_common_combination)

    print('\n(This calculation took:', '{:0,.2f}'.format((time.time() - start_time)), 'seconds.)')
    print('_'*70)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    sum_travel_time = np.sum(df['Trip Duration'])
    print ('Total travel time:', '{:,.1f}'.format(sum_travel_time/(60*60*24)), " Days")

    # display mean travel time

    mean_travel_time = np.mean(df['Trip Duration'])
    print('Average travel time per trip:', '{:,.1f}'.format(mean_travel_time/60), " Minutes")

    print('\n(This calculation took:', '{:0,.2f}'.format((time.time() - start_time)), 'seconds.)')
    print('_'*70)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_type = df.groupby('User Type')['User Type'].count().sort_values(ascending=False)
    print('\n',user_type)

    # Display counts of gender
    try:
      print("\n\n")
      gender_type = df.groupby('Gender')['Gender'].count().sort_values(ascending=False)
      print(gender_type)
      print('\n\n')
    except KeyError:
      print("\n\nGender:\nNo gender data available.")
    except:
      print("\n\nUnexpected Error during search for gender types.")

    labels ='male', 'female'
    try:
        counts_gender = df['Gender'].value_counts()
        colors = ["#1f77b4", 'lightskyblue']
        explode = (0.1, 0)
        plt.pie(counts_gender, labels=list(labels), explode=explode, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=60)
        plt.title("Gender Distribution in selected months / days")
        plt.show()
    except KeyError:
      print("\n\nGender:\nNo gender data is available for selection.")

    # Display earliest, most recent, and most common year of birth

    try:
      earliest_birth_year = np.min(df['Birth Year'])
      print('\n\n\nEarliest birth year:\n')
      print('{:04.0f}'.format(earliest_birth_year))
    except KeyError:
      print("\n\nEarliest birth year:\nSorry, no data available for selection.")
    except:
      print("\n\nUnexpected Error during search for years of birth.")

    try:
      latest_birth_year = np.max(df['Birth Year'])
      print('\n\nLatest birth year:\n')
      print('{:04.0f}'.format(latest_birth_year))
    except KeyError:
      print("\n\nLatest Birth year:\nSorry, no data available for your selection.")
    except:
      print("\n\nUnexpected Error during search for years of birth.")

    try:
      most_common_birth_year=df['Birth Year'].value_counts().idxmax()
      print('\n\nMost common birth year:\n')
      print('{:04.0f}'.format(most_common_birth_year))
    except KeyError:
      print("\n\nMost common birth year:\nSorry, no data available for your selection.")
    except:
      print("\n\nUnexpected Error during search for years of birth.")

    print('\n(This calculation took:', '{:0,.2f}'.format((time.time() - start_time)), 'seconds.)')
    print('_'*70)


def show_dataframe(df):

    qty_rows = 0
    show = input("Would you like to see the first ten rows of the data frame used for the calculations?\nPlease type 'yes' or 'no':\n\n").lower()
    while True:
        if show == 'no':
            return
        if show == 'yes':
            print(df[qty_rows: qty_rows + 10])
            qty_rows = qty_rows + 10
            show = input("Would you like to see ten more rows of the data frame used for the calculations?\nPlease type 'yes' or 'no':\n\n").lower()
        else:
            break


def main():

    while True:
        city = choose_city()
        month = choose_month()
        day=choose_day()
        df = load_choice(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_dataframe(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart == 'yes':
            continue
        else:
            break

if __name__ == "__main__":
    main()
