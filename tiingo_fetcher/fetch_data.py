import pandas as pd 
import requests
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


def fetch_stock(symbol, start_date, end_date, freq, api_key):
    """
    Fetch stock data from Tiingo.
    
    Parameters:
      symbol (str): Ticker symbol.
      start_date (str): Start date (YYYY-MM-DD).
      end_date (str): End date (YYYY-MM-DD).
      freq (str): Frequency - Supported values:
                 '1min' - one-minute bars
                 '5min' - five-minute bars
                 '15min' - fifteen-minute bars
                 '30min' - thirty-minute bars
                 '60min' - hourly bars
                 'daily' - daily bars
      api_key (str): Your Tiingo API key.
      
    Returns:
      data (pd.DataFrame): DataFrame with price data.
    """
    # Convert common frequency formats to Tiingo format
    freq_mapping = {
        '1min': '1min',
        '5min': '5min',
        '15min': '15min',
        '30min': '30min',
        '60min': '60min'
    }
    
    # Convert frequency if it's in the mapping
    tiingo_freq = freq_mapping.get(freq)
    if tiingo_freq is None:
        raise ValueError(f"Unsupported frequency: {freq}. Supported frequencies are: {list(freq_mapping.keys())}")
    
    url = f"https://api.tiingo.com/iex/{symbol}/prices"
    params = {
        'startDate': start_date,
        'endDate': end_date,
        'resampleFreq': tiingo_freq,
        'token': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    json_data = response.json()
    data = pd.DataFrame(json_data)
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'])
    return data


def generate_date_ranges(start_date, end_date):
    """
    Generate a list of monthly date ranges between start_date and end_date.
    
    Parameters:
        start_date (str or datetime): Start date
        end_date (str or datetime): End date
        
    Returns:
        list: List of tuples containing (start_date, end_date) for each month
    """
    # Convert string dates to date objects if needed
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    
    date_ranges = []
    current_date = start_date
    while current_date <= end_date:
        # Get last day of current month
        next_month = current_date + relativedelta(months=1)
        last_day = (next_month - relativedelta(days=1))
        
        # Ensure we don't exceed the end_date
        if last_day > end_date:
            last_day = end_date
            
        date_ranges.append((
            current_date.strftime('%Y-%m-%d'),
            last_day.strftime('%Y-%m-%d')
        ))
        
        # Move to first day of next month
        current_date = next_month
    
    return date_ranges


def fetch_data(symbol, key, start_date, end_date, freq):
    """
    Fetch and combine market data for a given symbol across multiple months.
    
    Parameters:
        symbol (str): Stock symbol to fetch data for
        key (str): Tiingo API key
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format
        freq (str): Data frequency (default '1min')
        
    Returns:
        pd.DataFrame: Combined DataFrame with all fetched data
    """
    dates = generate_date_ranges(start_date, end_date)
    sets = []

    for start, end in dates:
        data = fetch_stock(symbol, start, end, freq=freq, api_key=key)
        if 'date' in data.columns:
            data = data.sort_values('date').reset_index(drop=True)
        sets.append(data)
        print(f"Data fetched: {len(data)} rows from {start} to {end}")
    
    # Combine all DataFrames in sets
    combined_data = pd.concat(sets, ignore_index=True)
    return combined_data


