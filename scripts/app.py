import common
import extra
import constant

# Get Price Data from URL
price_data = common.get_data(constant.URL)['series'][0]['data']

# Format Date for each row
for i, date_and_price in enumerate(price_data):
    price_data[i][0] = common.format_date(date_and_price[0])

# Write daily prices to data folder
common.write_csv_file(constant.DAILY_PRICE_FILE_PATH, constant.HEADING, price_data)

#write monthly data to csv with normalization
common.write_csv_file(constant.MONTHLY_PRICE_FILE_PATH, constant.HEADING, extra.normalize_to_monthly(price_data))
