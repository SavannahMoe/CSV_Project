# 1 changing file to include all data from 2018
# 2. change the title to daily high and low temperature -2018
# 3 extract low temps from file and add to the chart

import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# the enumerated() function returns both the index of each item and the value of each item
# as you loop through the list
# zero based index meaning first thing is 0

for index, column_header in enumerate(header_row):
    print("Index", index, "Column Name:", column_header)

highs = []
dates = []
lows = []

# as an example
# somedate = '2018-07-01'
# converted_date = datetime.strptime(somedate, "%y-%m-%d")

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)


# print(highs)

# plot highs on a chart


import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
plt.title("Daily high and low temperatures for 2018", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Temperature in (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

fig.autofmt_xdate()

plt.show()


# matplotlib's pyplot API has a convenienve function called subplots(
# utiil)
# enclosing figure object, in a single cell

fig2, a = plt.subplots(2)
a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")

plt.show()