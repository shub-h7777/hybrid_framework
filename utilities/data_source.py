from utilities import read_utils

test_invalid_login_data = [
    ("saul", "saul123", "Invalid credentials"),
    ("kim", "kim123", "Invalid credentials"),
    ("john", "john123", "Invalid credentials")
]
#
# test_invalid_login_data1 = [
#     ["saul", "saul123", "Invalid credentials"],
#     ["kim", "kim123", "Invalid credentials"],
#     ["john", "john123", "Invalid credentials"]
# ]
#
# test_add_valid_employee_data = [
#     ["Admin", "admin123", "John", "J", "Wick", "John Wick", "John"],
#     ["Admin", "admin123", "Peter", "P", "Wick", "Peter Wick", "Peter"]
# ]


test_add_valid_employee_data =read_utils.get_sheet_as_file("../test_data/orange_test_data.xlsx","test_add_valid_employee")

test_add_invalid_profile_data=read_utils.get_sheet_as_file("../test_data/orange_test_data.xlsx","test_add_invalid_profile")