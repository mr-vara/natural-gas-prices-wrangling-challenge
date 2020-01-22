import urllib.request
import json
import csv

"""Get JSON data from the given url end-point.

:param url: string that contains URL of the resource
:returns: json data
"""
def get_data(url):
    dataURL = urllib.request.urlopen(url)
    data = dataURL.read()
    encoding = dataURL.info().get_content_charset('utf-8')
    return json.loads(data.decode(encoding))

"""Write CSV file to given path with given headings and data.

:param path: string that contains local path where the CSV file need to be saved
:param headings: list that contains headings of the CSV file
:param data: list that contains data of the CSV file
"""
def write_csv_file(path, headings, data):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headings)
        writer.writerows(data)

"""Format Date (YYYY-MM-DD) from string (YYYYMMDD).

:param date: string of date in YYYYMMDD format
:returns: string formatted date YYYY-MM-DD
"""
def format_date(date):
    return date[0:4]+'-'+date[4:6]+'-'+date[6:8]
