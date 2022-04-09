# with open("weather_data.csv") as file_data: #will open a file with name weather_data and data will store in new file name data
#     data = file_data.readlines()
#     print(data)  # result = ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,15,Rain\n', 'Wednesday,14,Sunny\n', 'Thursday,15,Cloudy\n', 'Friday,19,Sunny\n', 'Saturday,13,Rain\n',
#
#     #OLD_METHOD


# import csv
#
# with open("weather_data.csv") as file_data:
#     data = csv.reader(file_data)
#     temperatures = []  #will initialise a blank list after that which will contain all data
#
#     for row in data:
#         if(row[1] != "temp"):  #this will check where all the temp will store in list except level
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")

print(data)  # will print whole data

print(data["temp"]) #will print the data in that particular column

