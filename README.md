# Natural gas prices [![Python version](https://img.shields.io/badge/python-3.%2B-red.svg)](https://www.python.org/downloads/release/python-381/) [![OKFN](https://img.shields.io/badge/data-OKFN-green.svg)](https://data.okfn.org/tools/view?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmr-vara%2Fnatural-gas-prices-wrangling-challenge%2Fmaster%2Fdatapackage.json) [![Chart](https://img.shields.io/badge/canvasjs-chart-blue.svg)](https://mr-vara.github.io/henry-hub/index.html)
Data Wrangling on Henry Hub Natural Gas Spot Prices. (Units: Dollars per Million Btu). The data is downloaded from United States Energy Information Administration website https://www.eia.gov

## Data
The Henry hub natural gas spot prices are available in both daily and monthly granularities. Please check `data` directory for the `csv` files.
View the data in OKFN Data Package Viewer [here](https://data.okfn.org/tools/view?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmr-vara%2Fnatural-gas-prices-wrangling-challenge%2Fmaster%2Fdatapackage.json)

You can also check chart [here](https://mr-vara.github.io/henry-hub/index.html)

## Running Scripts

Run following command in your terminal:

```sh
$ python3 scripts/app.py
```
Note: Make sure you have Python version `3.x` installed.

### Running Unit Tests

Run following command in your terminal:

```sh
$ python3 scripts/tests.py
```

## Project structure

### Directory Structure

 Top-leve directory layout of the project

    .
    ├── data                    # Contains CSV files
    ├── scripts                 # Contains Python script files
    ├── datapackage.json
    └── README.md

 Directory layout of `data` which contains CSV files

    .
    ├── ...
    ├── data                                    # CSV files
    │   ├── henry_hub_daily_prices.csv          # Daily prices CSV file
    │   └── henry_hub_monthly_prices.csv        # Monthly prices CSV file
    └── ...

 Directory layout of `scripts` which contains Python script files

    .
    ├── ...
    ├── scripts               # Script files
    │   ├── app.py            # Main Script file
    │   ├── common.py         # Module that contains common methods like read file, write file, date format etc.,
    │   ├── constant.py       # Contains constants used in the project
    │   ├── extra.py          # Contains extra methods used in the project like normalizing daily granularities to monthly granularities 
    │   └── tests.py          # Contains tests
    └── ...


### Dependencies

- [statistics](https://docs.python.org/3.4/library/statistics.html): Used for statistics operations like mean.
- [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request): Used for read data from URL.
- [csv](https://docs.python.org/3/library/csv.html): Used for CSV file read/write operations.
- [json](https://docs.python.org/3/library/json.html): Used for JSON Encoding and Decoding.
- [unittest](https://docs.python.org/3/library/unittest.html): Unit Testing Framework.
