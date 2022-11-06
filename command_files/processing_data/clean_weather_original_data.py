import re

file_to_clear = r'..\..\analysis_data\weather_original_data.txt'
cleaned_file = r'..\..\analysis_data\cleaned_weather.txt'

# Making sure our "cleaned" file is empty
open(cleaned_file, 'w').close()

temp_memory = []
with open(file_to_clear) as file:
    for line in file:
        station_id = line[0:11]
        year = line[11:15]
        month = line[15:17]
        var_name = line[17:21]
        data = line[21:]

        cleaned_data = re.sub(r"(?!-(?=\d))[^0-9 ]", " ", data)
        cleaned_data = cleaned_data.split()
        cleaned_data = ' '.join(cleaned_data)
        temp_memory.append(station_id + ' ' + year + ' ' + month + ' ' + var_name + ' ' + cleaned_data + '\n')

    with open(cleaned_file, 'w') as clear_file:
        clear_file.writelines(temp_memory)
