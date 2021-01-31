import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH = ['all', 'january', 'february', 'march', 'april', 
         'may', 'june']
DAYS = ['all', 'sunday','monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday']

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    key=CITY_DATA.keys()
    city=input('Please enter city name: ')
    while city.lower() not in key:
        print ('This is not the correct city name!!! Please try again')
        city=input('Please enter city name again: ')
    if city.lower() in key:
        print('Now its time to enter month: ')
        month = input('Please enter month: ')
        while month.lower() not in MONTH:
            print('Please check the month again!!')
            month = input('Please enter the month again: ')
        print('Now its time to enter day: ')
        day = input('Please enter day name: ')
        while day.lower() not in DAYS:
            print('Please check the day again!!')
            day = input('Please enter day name again: ')
    print('-'*40)
    return city, month, day
      
def load_data(city, month, day):
  df = pd.read_csv(CITY_DATA[city.lower()])
  df['Start Time'] = pd.to_datetime(df['Start Time'])
  df['month'] = df['Start Time'].dt.month
  df['day'] = df['Start Time'].dt.weekday_name
  
  if month != 'all':
      month = MONTH.index(month)+1
      df = df[df['month'] == month]
    
  if day != 'all':
      df = df[df['day'] == day.title()]
  return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month from the Start Time column 
    df['month'] = df['Start Time'].dt.month
    popular_month =  df['month'].mode()[0]
    month_name = MONTH[popular_month-1]
    popular_month_count = df['month'].value_counts().max()
    print ("Most common month and count are: ",  month_name, popular_month_count)
    
    # extract day of week from the Start Time column 
    df['day'] = df['Start Time'].dt.weekday_name
    popular_day =  df['day'].mode()[0]
    popular_day_count = df['day'].value_counts().max()
    print ("Most common day and count are: ",popular_day, popular_day_count )
    
    # extract hour from the Start Time column 
    df['hour'] = df['Start Time'].dt.hour
    popular_hour =  df['hour'].mode()[0]
    popular_hour_count = df['hour'].value_counts().max()
    print ("Most common hour and count are: ",popular_hour, popular_hour_count)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    count = df['Start Station'].value_counts().max()
    print ('Most common start station is: ',most_common_start_station, count)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    count1 = df['End Station'].value_counts().max()
    print ('Most common end station is: ',most_common_end_station, count1)

    # display most frequent combination of start station and end station trip
    most_freq_combo = (df['Start Station']+df['End Station']).mode()[0]
    print ('Most frequent combination is: ',most_freq_combo)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ('Total travel time is: ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print ('Mean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print ('Count of user types is: ',count_user_types)
    print (' ')
    
    # Display counts of gender
    count_gender = df['Gender'].value_counts()
    print ('Count of gender is: ',count_gender)
    print (' ')
    
    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()
    print ('Earliest birth year is: ',earliest_birth_year)
    
    recent_birth_year = df['Birth Year'].max()
    print ('Recent birth year is: ',recent_birth_year)
    
    common_birth_year = df['Birth Year'].mode()[0]
    print ('Common birth year is: ',common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
  while True:
    city, month, day = get_filters()
    df = load_data(city, month, day)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
          
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
      break
if __name__=='__main__':
  main()              
               