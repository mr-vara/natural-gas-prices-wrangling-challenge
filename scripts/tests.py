import unittest
import os
import constant

class TestFileExists(unittest.TestCase):

    def test_daily_file_exists(self):
        self.assertTrue(os.path.isfile(constant.DAILY_PRICE_FILE_PATH))

    def test_monthly_file_exists(self):
        self.assertTrue(os.path.isfile(constant.MONTHLY_PRICE_FILE_PATH))

if __name__ == '__main__':
    unittest.main()