# with open("weather_data.csv") as file:
#     contents = file.readlines()
#     print(contents[1])

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(sum(temp_list) / len(temp_list))
# print(data['temp'].mean())
# print(data['temp'].max())
#
# Get data in column
# print(data['condition'])
# print(data.condition)

# Get data in row
# print(data[data.day == "Tuesday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(int(monday.temp) * 1.8 + 32)

# Create dataframe from scratch
data_scratch = {
    "students": ["Amy", "James", "Bob"],
    "score": [94, 74, 89]
}

data = pandas.DataFrame(data_scratch)
data.to_csv("new_data.csv")
