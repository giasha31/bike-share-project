import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input("Enter city name (Chicago, New York City, Washington):\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter a valid city.")

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Enter month (January to June) or 'all':\n").lower()
        if month in months:
            break
        else:
            print("Invalid input. Please enter a valid month.")

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Enter day of week or 'all':\n").lower()
        if day in days:
            break
        else:
            print("Invalid input. Please enter a valid day.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        city (str): name of the city to analyze
        month (str): name of the month to filter by, or "all"
        day (str): name of the day to filter by, or "all"

    Returns:
        df (DataFrame): Pandas DataFrame containing filtered city data
    """
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' column to datetime for easy time filtering
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        df (DataFrame): The dataframe containing bikeshare data.

    Returns:
        None
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('Most Common Month:', df['month'].mode()[0].title())
    print('Most Common Day of Week:', df['day_of_week'].mode()[0].title())
    print('Most Common Start Hour:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """
    Displays statistics on the most popular stations and trips.

    Args:
        df (DataFrame): The dataframe containing bikeshare data.

    Returns:
        None
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('Most Common Start Station:', df['Start Station'].mode()[0])
    print('Most Common End Station:', df['End Station'].mode()[0])
    df['Trip'] = df['Start Station'] + " -> " + df['End Station']
    print('Most Common Trip:', df['Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('Total Travel Time:', df['Trip Duration'].sum())
    print('Average Travel Time:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('User Types:\n', df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print('\nGender:\n', df['Gender'].value_counts())
    else:
        print('\nNo gender data available.')

    if 'Birth Year' in df.columns:
        print('\nEarliest Birth Year:', int(df['Birth Year'].min()))
        print('Most Recent Birth Year:', int(df['Birth Year'].max()))
        print('Most Common Birth Year:', int(df['Birth Year'].mode()[0]))
    else:
        print('\nNo birth year data available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    row_index = 0
    while True:
        raw = input('\nWould you like to see 5 rows of raw data? Enter yes or no:\n').lower()
        if raw != 'yes':
            break
        print(df.iloc[row_index:row_index+5])
        row_index += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no:\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
# This is the final version submitted to Udacity | 2nd of July

