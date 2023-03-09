""" learning the CSV data interference """

import pandas

df=pandas.read_csv(filepath_or_buffer="../test_data/test_invalid_login_data.csv", delimiter=";")
print(df.values)

