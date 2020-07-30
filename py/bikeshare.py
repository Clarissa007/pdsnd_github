#import modules from library

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

TIME_DATA = {'month', 'day', 'both', 'none'}
MONTH_DATA = {'january', 'february', 'march', 'april', 'may', 'june'}
DAY_DATA = {'1': 'monday', '2': 'tuesday', '3': 'wednesday', '4': 'thursday', '5': 'friday', '6': 'saturday',
            '7': 'sunday'}


def get_filters():

   

    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input("Would you like to see data for Chicago, New York or Washington?\n").lower()
        if city not in CITY_DATA:
            print("\nInvalid answer\n")
            continue
        else:
            break

    while True:
        time = input("Would you like to filter the data by month, day, both or not at all? Type \"none\" for no time filter.\n").lower()
        if time not in TIME_DATA:
            print("\nError! Please type it again.")
            continue

        elif time == 'month':
            month = input("Which month? January, February, March, April, May or June? \n").lower()
            if month not in MONTH_DATA:
                print("\nError! Please type it again.")
                continue

            day = 'all'
            break

        elif time == 'day':
            month = 'all'
            day = input("Which day? Please type your response as an integer (e.g., 1 = Monday \n")
            if day not in DAY_DATA:
                print("\nError! Please type it again.")
                continue
            break

        elif time == 'both':
            month = input("Which month? January, February, March, April, May or June? \n").lower()
            if time not in TIME_DATA:
                print("\nError! Please type it again.")
                continue

            day = input("Which day? Please type your response as an integer (e.g., 1 = Sunday \n")
            if day not in DAY_DATA:
                print("\nError! Please type it again.")
                continue
            break

        elif time == "none":
            month = 'all'
            day = 'all'
            break
        else:
            break

    if day != 'all':
        day = DAY_DATA[day]


    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    return df

def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']

    print('The most common month for travel is {}'.format(months[most_common_month-1]))

    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week for travel is {}'.format(most_common_day_of_week))

    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour for travel is {}'.format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    ##Displays statistics on the most popular stations and trip

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start = df['Start Station'].mode()[0]
    print('Most commonly used start station is {}'.format(common_start))

    common_end = df['End Station'].mode()[0]
    print('Most commonly used end station is {}'.format(common_end))

    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print('The most frequent combination of trips are from {}'.format(common_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    #Displays statistics on the total and average trip duration.

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel = df['Trip Duration'].sum()
    sum_seconds = total_travel % 60
    sum_minutes = total_travel // 60 % 60
    sum_hours = total_travel // 3600 % 60
    sum_days = total_travel // 24 // 3600
    print('Total trip duration is {} days, {} hours, {} minutes and {} seconds'.format(sum_days, sum_hours, sum_minutes, sum_seconds))
    mean_travel = df['Trip Duration'].mean()
    mean_seconds = mean_travel % 60
    mean_minutes = mean_travel // 60 % 60
    mean_hours = mean_travel // 3600 % 60

    print('Average trip duration is {} hours, {} minutes and {} seconds'.format(mean_hours, mean_minutes, mean_seconds))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The types of users by number are given below:\n\n{}'.format(user_types))
    print('.' * 20)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('The types of users by gender are given below:\n\n{}'.format(gender))

    else:
        print("There is no gender information in this city.")

    print('.' * 20)
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        print('Earliest year of birth was {}.'.format(earliest))

        recent = df['Birth Year'].max()
        print('Most recent year of birth was {}.'.format(recent))

        common_birth = df['Birth Year'].mode()[0]
        print('Most common year of birth year was {}.'.format(common_birth))

    else:
        print("There is no birth year information in this city.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    start = 0
    end = 5

    rawstart = input("Do you want to see the raw data? (y)es / (n)o\n").lower()

    if rawstart == 'yes' or rawstart == 'y':
        while end <= df.shape[0] - 1:

            print(df.iloc[start:end,:])
            start += 5
            end += 5

            rawend = input("Do you wish to continue? (y)es / (n)o\n").lower()
            if rawend == 'no' or rawend == 'n':
                break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter (y)es or (n)o\n')
        if restart.lower() == 'no' or restart.lower() == 'n':
            break


if __name__ == "__main__":
    main()
