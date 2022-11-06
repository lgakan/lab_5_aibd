import pandas as pd

# data_file = r'..\..\analysis_data\cleaned_weather.txt'

station_id = []
year = []
month = []
var_name = []
data = []


def answer(data_file):
    with open(data_file) as file:
        line_counter = 0
        for line in file:
            split_line = line.split(' ', 4)
            station_id.append(split_line[0])
            year.append(split_line[1])
            month.append(split_line[2])
            var_name.append(split_line[3])
            string_data = split_line[4][0:-1]

            string_data = string_data.replace('-9999', 'None')
            string_data = string_data.split()
            data.append([eval(i) for i in string_data])
            line_counter += 1


    df_date = pd.DataFrame({'date_id': [i for i in range(0, len(year * 31))],
                            'year': [x for x in year for i in [x] * 31],
                            'month': [x for x in month for i in [x] * 31],
                            'day': line_counter * [i for i in range(1, 32)]})

    date_id = df_date['date_id']

    df_values = pd.DataFrame({'measurement_id': [i for i in range(0, len(year * 31))],
                              'date_id': date_id,
                              'variable': [x for x in var_name for i in [x] * 31],
                              'value': [a for n in data for a in n]})

    return df_date, df_values

