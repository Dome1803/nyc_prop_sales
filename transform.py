"""
This script transforms a csv file with stock data and writes the results
to disk.
"""

# Imports
import pandas as pd
import functions as fc
import numpy as np
import datetime as dt

def _transform():
    """
    This function performs the transformation.
    :return: None.
    """
    input_file = "data/nyc-rolling-sales.csv"
    output_file = "data/nyc-rolling-sales2.csv"

    # Read input data
    print("Reading file from:", input_file, "\n")
    sales_frame = fc.read_csv(input_file)
    print(sales_frame.head().to_string(), "\n")

    # Perform transformation
    print("Performing transformation...", "\n")

    # Dropping unnecessary column
    sales_frame = sales_frame.drop(["Unnamed: 0"], axis=1)

    # Changing format of boroughs to string (from int)
    sales_frame["BOROUGH"] = sales_frame["BOROUGH"].apply(str)

    # Replacing numbers of boroughs with actual name
    sales_frame["BOROUGH"] = sales_frame["BOROUGH"].replace(["1"], "Manhattan")
    sales_frame["BOROUGH"] = sales_frame["BOROUGH"].replace(["2"], "Brooklyn")
    sales_frame["BOROUGH"] = sales_frame["BOROUGH"].replace(["3"], "Queens")
    sales_frame["BOROUGH"] = sales_frame["BOROUGH"].replace(["4"], "The Bronx")
    sales_frame["BOROUGH"] = sales_frame["BOROUGH"].replace(["5"], "Staten Island")

    # Replacing the " -  " filler and changing format of sale price to numeric (from str)
    sales_frame["SALE PRICE"] = sales_frame["SALE PRICE"].replace([" -  "], "0")
    sales_frame["SALE PRICE"] = pd.to_numeric(sales_frame["SALE PRICE"])

    # Changing format of sale date to datetime (from str)
    #sales_frame["SALE DATE"] = pd.to_datetime(sales_frame["SALE DATE"])
    sales_frame["SALE DATE"] = sales_frame["SALE DATE"].apply(pd.to_datetime, format="%Y-%m-%d %H:%M:%S")

    # Replacing the " -  " filler in columns LSF and GSF
    sales_frame["LAND SQUARE FEET"] = sales_frame["LAND SQUARE FEET"].replace([" -  "], "0")
    sales_frame["GROSS SQUARE FEET"] = sales_frame["GROSS SQUARE FEET"].replace([" -  "], "0")

    # Changing LSF and GSF to numeric values (from str)
    sales_frame["LAND SQUARE FEET"] = pd.to_numeric(sales_frame["LAND SQUARE FEET"])
    sales_frame["GROSS SQUARE FEET"] = pd.to_numeric(sales_frame["GROSS SQUARE FEET"])

    # Adjusting square feet to square meter / column names stay the same for now
    sales_frame["LAND SQUARE FEET"] = fc.to_qm(sales_frame["LAND SQUARE FEET"])
    sales_frame["GROSS SQUARE FEET"] = fc.to_qm(sales_frame["GROSS SQUARE FEET"])

    # Write results to disk
    print("Writing results to:", output_file, "\n")
    print(sales_frame.head().to_string(), "\n")

    fc.to_csv(output_file, sales_frame)
    print("Export successful!\n", sales_frame.dtypes)


# This statement executes the script
if __name__ == "__main__":
    _transform()