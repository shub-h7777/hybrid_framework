""" learning the CSV data interference """

import pandas

import utilities.read_utils

df=pandas.read_csv(filepath_or_buffer="../test_data/test_invalid_login_data.csv", delimiter=";")
print(df.values)

utilities.read_utils.get_sheet_as_file("../test_data/orange_test_data.xlsx")