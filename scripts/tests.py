import os
import csv
import unittest
import constant
import common
import extra

def make_float(x):
	if(x):
		return float(x)

class TestFileExists(unittest.TestCase):

	def test_daily_file_exists(self):
		self.assertTrue(os.path.isfile(constant.DAILY_PRICE_FILE_PATH))

	def test_monthly_file_exists(self):
		self.assertTrue(os.path.isfile(constant.MONTHLY_PRICE_FILE_PATH))

	def test_csv_file_contents(self):
		# Read CSV File contents and convert prices from string to float, then keep it in a dict
		with open(constant.DAILY_PRICE_FILE_PATH, mode='r') as csv_file:
			reader = csv.reader(csv_file)
			next(reader, None)
			csv_file_contents = {rows[0]:make_float(rows[1]) for rows in reader}

		# Get data from URL and keep it in a dict
		price_data = common.get_data(constant.URL)['series'][0]['data']
		price_data_dict = {}
		for i, date_and_price in enumerate(price_data):
			price_data[i][0] = common.format_date(date_and_price[0])
			price_data_dict[price_data[i][0]] = price_data[i][1]

		# Assert both data is equal
		self.assertTrue(csv_file_contents == price_data_dict)

if __name__ == '__main__':
	unittest.main()