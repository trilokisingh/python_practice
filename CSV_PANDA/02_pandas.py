import pandas

# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()  # data will convert into dictionary
#
# #  print(data_dict)
# # *********************************************************************************************
# temp_list = data["temp"].to_list()  # particular column wil turn into list
# max = data["temp"].max()  # will return the maximum value
# print(max)
# avrg = data["temp"].mean()  # this will also calculate the mean or avg temperature
# print(avrg)
# avg = sum(temp_list)/len(temp_list)
# print(f"the avg temperature is {avg}")
# #   print(avg)
#
# # ******************************************************************************************************************
# column = data[data.day == "Monday"]   # inside data frame day will match and according to that day row will print
# print(column)
#
# print(data[data.temp == data.temp.max()])  # will return highest temp
# print(data[data.temp == 13])


# ******************************************************************


student_Marks = {  "students":["aman","rajat","vinay","codex","divill"],
                  "marks" : [15,50,82,40,60],
                  "age" :[17,16,19,19,20]
}

# marks = pandas.DataFrame(student_Marks)
# print(marks)

s_data_frame = pandas.DataFrame(student_Marks)
print(s_data_frame)

s_data_frame.to_csv("new_s_csv")  # export a niw file with name new_s_csv which will csv

