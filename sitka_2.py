# adding dates to file
import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# the enumerated() function returns both the index of each item and the value of each item
# as you loop through the list
# zero based index meaning first thing is 0

for index, column_header in enumerate(header_row):
    print("Index", index, "Column Name:", column_header)

highs = []
dates = []

# as an example
# somedate = '2018-07-01'
# converted_date = datetime.strptime(somedate, "%y-%m-%d")

for row in csv_file:
    highs.append(int(row[5]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)


# print(highs)

# plot highs on a chart


import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Temperature in (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

fig.autofmt_xdate()

plt.show()
