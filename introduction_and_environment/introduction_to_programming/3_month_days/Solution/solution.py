month_dict = {}
month_dict['January'] = 31
month_dict['February'] = 28
month_dict['March'] = 31
month_dict['April'] = 30
month_dict['May'] = 31
month_dict['June'] = 30
month_dict['July'] = 31
month_dict['August'] = 31
month_dict['September'] = 30
month_dict['October'] = 31
month_dict['November'] = 30
month_dict['December'] = 31

month = input('Enter month: ')
data = 0
if month in month_dict:
    data = month_dict[month]
print(data)