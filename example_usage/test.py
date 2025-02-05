

from tiingo_fetcher.fetch_data import fetch_data

data = fetch_data("AAPL",'Your key' , "2023-01-01", "2023-02-01", '1min')

print(data.head())
