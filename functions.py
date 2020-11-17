"""
This module provides helper methods to analyze sales
"""

# Imports
import pandas as pd



def read_csv(file_name):
    """
    This function reads a CSV file in German format.
    :param file_name: The file name.
    :return: A data frame with the contents.
    """
    return pd.read_csv(file_name, sep=",")


def to_csv(file_name, data_frame):
    data_frame.to_csv(file_name, sep=",", index=False)

def to_datetime(data_frame):
    pd.to_datetime(data_frame, errors="coerce")