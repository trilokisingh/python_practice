# In this programm we will make a program where we will use a csv file name "2018_central_park......."
# from this file we will extract data of black gray and cinnonon color
# and total numbers of color and put the into a new file


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_Color_Count = len(data[data["Primary Fur Color"] == "Gray"])
black_Color_Count = len(data[data["Primary Fur Color"] == "Black"])
Cinnamon_Color_Count = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(gray_Color_Count)
print(black_Color_Count)
print(Cinnamon_Color_Count)


#this is new dict which will store the new data in formate  of  dictionary
data_dict = {
    "fur color":["Gray","Black","Cinnamon"],
    "count":[gray_Color_Count,black_Color_Count,Cinnamon_Color_Count]
}

# in this dictionary will formate in DataFrame

new_Data = pandas.DataFrame(data_dict)
print(new_Data)

new_Data.to_csv("final_csv")
