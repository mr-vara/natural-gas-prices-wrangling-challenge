import statistics

"""Normalize the daily prices data to months.

:param data: list that contains daily prices data
:returns: monthly_data list with start date and average price of the particular month
"""
def normalize_to_monthly(data):
    data_dict = {}
    # Group prices based on YYYYMM
    for date_and_price in data:
        yyyy_mm = date_and_price[0][0:7]
        dd = date_and_price[0][8:10]
        if yyyy_mm not in data_dict:
            data_dict[yyyy_mm] = []
        data_dict[yyyy_mm].append([int(dd),date_and_price[1] or 0])

    # Reduce data to start date and average price
    monthly_data_dict = {}
    for key, date_and_price in data_dict.items():
        date, price = map(list, zip(*date_and_price))
        monthly_data_dict[key] = {'start_date': min(date), 'average': round(statistics.mean(price), 2)}
    
    # Format the monthly data to a list used to write CSV file
    monthly_data = []
    for key, date_and_avg in monthly_data_dict.items():
        monthly_data.append([key+'-'+str(date_and_avg['start_date']),date_and_avg['average']])
    
    return monthly_data
