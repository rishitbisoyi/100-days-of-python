# with open ("25_CSVFiles/Basics/weather_data.csv", "r") as file:
#     data = file.readlines()
# print(data)

# import csv

# with open ("25_CSVFiles/Basics/weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

# import pandas as pd
# data = pd.read_csv("25_CSVFiles/Basics/weather_data.csv")
# print(data["temp"])

# temp_list=data["temp"].to_list()
# print(f"{sum(temp_list)/len(temp_list):.2f}")
# print(f"{data["temp"].mean():.2f}")
# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])
# print(data.condition[data.temp == data.temp.max()])

# t=data[data.day == "Monday"]
# print(t.condition)

import pandas as pd
data = pd.read_csv("25_CSVFiles/Basics/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
print(df)
df.to_csv("25_CSVFiles/Basics/squirrel_count.csv", index=False)