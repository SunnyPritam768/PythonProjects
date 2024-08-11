import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data)

print("\n")

print(data["temp"])

print("\n")

data_to_dict = data.to_dict()
print(data_to_dict)

print("\n")
data_to_list = data["temp"].to_list()
print(data_to_list)

length_of_temp_list = len(data_to_list)
sums = 0
for value in range(0, len(data_to_list)):
    sums += data_to_list[value]

print("\n")
average_temperature = sums/length_of_temp_list
print(average_temperature)

print("\n")
#  We can also do this in one line
print(data["temp"].mean())

# How to get maximum temperature wali row
print(data[data["temp"] == data["temp"].max()])

