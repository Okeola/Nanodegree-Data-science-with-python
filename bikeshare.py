#Name:OKEOLA Abass
#email:abassokeola@gmail.com

import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import time


# Get the name of the city to explore
def city_name ():
    '''Inform user to specify city of interest, returns the filename for that city's bike share data.
    Args:none.
    Returns: Filename for a city's bikeshare data.'''
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('\n Welcome! Lets get some insight into the US bikeshare data!\n'
                     'Will you like to see data for any of these three cities Chicago, New York, or'
                     ' Washington?\n')
        if city.lower() == 'chicago':
            return 'chicago.csv'
        elif city.lower() == 'new york':
            return 'new_york_city.csv'
        elif city.lower() == 'washington':
            return 'washington.csv'
        else:
            print('Sorry, I do not understand your input. Please input either '
                  'Chicago, New York, or Washington.')

# Get the filter criteria
def get_filter_period():
    '''Asks the user for the time period filter.
    Args:
        none.
    Returns:
        (str) duration filter for the bikeshare data.
    '''
    time_period = ''
    while time_period.lower() not in ['month', 'day', 'none']:
        time_period = input('\n Will you like to filter the bike by month or day, Type "none" for no time filter.\n')
        if time_period.lower() not in ['month', 'day', 'none']:
            print('Sorry, I do not understand your input.')
    return time_period


# Get specified month
def get_month():
    '''Asks the user for a month and returns the specified month.
    Args:
        none.
    Returns:
        Lower and upper limit of month for the bikeshare data.
    '''
    month_input = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month_input.lower() not in months_dict.keys():
        month_input = input('\nWhich month? January, February, March, April,'
                            ' May, or June?\n')
        if month_input.lower() not in months_dict.keys():
            print('Sorry, month not in the database. Please type in a month between January and June')
    month = months_dict[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))

# Get specified day
def get_day():
    ''' Request  the user for a day.
    Args:   none.
    Returns: upper and lower limit of date for the bikeshare data.
    '''
    this_month = get_month()[0]  
    month = int(this_month[5:])
    valid_date = False
    while valid_date == False:    
        inte = False
        day = input('\nWhich day? Please type your response as an integer.\n')
        while inte == False:
            try:
                day = int(day)
                inte = True
            except ValueError:
                print('Error, kindly type your response as an integer.')
                day = input('\n Specify day? Please type your response as an integer.\n')
        try:
            start_date = datetime(2017, month, day)
            valid_date = True
        except ValueError as e:
            print(str(e).capitalize())
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))


# Get most popular month
def popu_month(df):
    '''Finds the most popular month for start time column.
    Args:   bikeshare dataframe
    Returns:
        none
    '''
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['start_time'].dt.month.mode())
    pop_month = months[index - 1]
    print('The most popular month is {}.'.format(pop_month))
    
# Get most popular day
def popu_day(df):
    '''Finds the most popular day of week for start time column.
    Args: bikeshare dataframe
    Returns: none
    '''
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday', 'Sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    mostpop_day = days_of_week[index]
    print('The most popular day of week for start time is {}.'.format(mostpop_day))

    
# Get most popular hour
def popu_hour(df):
    '''Finds the most popular hour of day for start time.
    Args: bikeshare dataframe
    Returns:none
    '''
    pop_hour = int(df['start_time'].dt.hour.mode())
    if  pop_hour == 0:
        am_pm = 'am'
        pop_hour_read = 12
    elif 1 <= pop_hour < 13:
        am_pm = 'am'
        pop_hour_read = pop_hour
    elif 13 <= pop_hour < 24:
        am_pm = 'pm'
        pop_hour_read = pop_hour - 12
    print('The most popular hour of day for start time is {}{}.'.format(pop_hour_read, am_pm))

    
# Get trip duration 
def trip_duration(df):
    '''Find the total and average trip duration in hours, minutes, and seconds.
    Args:bikeshare dataframe
    Returns: none
    '''
    total_duration = df['trip_duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {} seconds.'.format(hour, minute, second))
    average_duration = round(df['trip_duration'].mean())
    mi, se = divmod(average_duration, 60)
    if mi > 60:
        hr, mi = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(hr, mi, si))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(mi, se))

 # Get most popular station
def popu_stations(df):
    '''Find the most popular start station and most popular end station.
    Args: bikeshare dataframe
    Returns: none
    '''
    pop_start = df['start_station'].mode().to_string(index = False)
    pop_end = df['end_station'].mode().to_string(index = False)
    print('The most popular start station is {}.'.format(pop_start))
    print('The most popular end station is {}.'.format(pop_end))

    # Get most popular trip
def popu_trip(df):
    '''Finds the most popular trip.
    Args: bikeshare dataframe
    Returns: none
    '''
    pop_trip = df['journey'].mode().to_string(index = False)
    # The 'journey' column is created in the statistics() function.
    print('The most popular trip is {}.'.format(pop_trip))

    
    
# Get the type and number of users
def users(df):
    '''Finds  the counts of each user type.
    Args:bikeshare dataframe
    Returns: none
    '''
    subscriber = df.query('user_type == "Subscriber"').user_type.count()
    customer = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subscriber, customer))

    
# Get gender distribution
def gender(df):
    '''Finds  the counts of gender.
    Args:bikeshare dataframe
    Returns: none
    '''
    male_count = df.query('gender == "Male"').gender.count()
    female_count = df.query('gender == "Male"').gender.count()
    print('There are {} male users and {} female users.'.format(male_count, female_count))

    
# Get the birth years   
def birth_years(df):
    ''' Findsthe earliest age of olderst user), and and most popular birth years.
    Args: bikeshare dataframe
    Returns: none
    '''
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest bike users are born in {}.\n The youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(earliest, latest, mode))

    
# Get the data lines to be displayed
def display_data(df):
    '''This displays seven lines of data, if specified by the user.
    After displaying seven lines, the user can see seven more, until they say stop.
    Args: data frame
    Returns: none
    '''
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    upper = 0
    lower = 7
    valid_input = False
    while valid_input == False:
        display = input('\n Will you like to see individual trip data? Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Error!, I do not understand your input. Please type 'yes' or 'no'.")
    if display.lower() == 'yes': # prints every column except the 'journey' column created in statistics()
        print(df[df.columns[0:-1]].iloc[upper:lower])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\n Will you like to view more individual trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Sorry, I do not understand your input. Please type'yes' or 'no'.")
            if display_more.lower() == 'yes':
                upper += 7
                lower += 7
                print(df[df.columns[0:-1]].iloc[upper:lower])
            elif display_more.lower() == 'no':
                break


def statistics():
    '''Compute descriptive statistics and print out the output for each city and
    time period as desired by the user as input data
    Args: none.
    Returns: none.
    '''
    # Apply filter.filter by city "Chicago, New York, or Washington"
    city = city_name()
    print(' Data loading....please wait...')
    df = pd.read_csv(city, parse_dates = ['Start Time', 'End Time'])
    
    # Create new label.change all column names to lowercase letters and replace spaces with underscores
    new_labels = []
    for col in df.columns:
        new_labels.append(col.replace(' ', '_').lower())
    df.columns = new_labels
    
    # To fully display the column. Adjust column width so that the long strings in the 'journey'
    pd.set_option('max_colwidth', 50)
    
    # make a new column 'journey'that concatenates 'start_station' with 'end_station' 
    df['journey'] = df['start_station'].str.cat(df['end_station'], sep=' to ')

    # Now Filter by month, day, none
    time_period = get_filter_period()
    if time_period == 'none':
        df_filtered = df
    elif time_period == 'month' or time_period == 'day':
        if time_period == 'month':
            filter_lower, filter_upper = get_month()
        elif time_period == 'day':
            filter_lower, filter_upper = get_day()
        print('data currently being filtered data...')
        df_filtered = df[(df['start_time'] >= filter_lower) & (df['start_time'] < filter_upper)]
    print('\n Computing the first statistical description...')

    if time_period == 'none':
        start_time = time.time()
        
        # print the duration of the most popular month for start time
        popu_month(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistical description...")
    
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # Print the most popular day of week for start time
        popu_day(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\n Calculating the next statistical description...")    
        start_time = time.time()

    # print the most popular hour of day for start time
    popu_hour(df_filtered)
    start_time = time.time()
    print("That took %s seconds." % (time.time() - start_time))
    print("\n Calculating the next statistical description...")
    

    # print the total and average trip duration
    trip_duration(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\n Calculating the next statistical description...")
    start_time = time.time()

    # print the most popular start and end station
    print("That took %s seconds." % (time.time() - start_time))
    print("\n Calculating the next statistical description...")
    start_time = time.time()

    # What is the most popular trip?
    popu_trip(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\n Calculating the next statistical description...")
    start_time = time.time()

    # What are the counts of each user type?
    users(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        print("\n Calculating the next statistical description...")
        start_time = time.time()
        
        # What are the counts of gender?
        gender(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\n Calculating the next statistical description...")
        start_time = time.time()

        # print the oldest and youngest user
        birth_years(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))

    # Display seven lines of data at a time if user specifies that they would like to see it
    display_data(df_filtered)

    # Accomodate for restarting of the inquiry
    restart = input('\n Will you like to restart? Type \'yes\' or \'no\'.\n')
    while restart.lower() not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()