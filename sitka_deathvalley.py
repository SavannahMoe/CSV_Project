# 1 changing file to include all data from 2018
# 2. change the title to daily high and low temperature -2018
# 3 extract low temps from file and add to the chart

import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")
open_file = open("death_valley_2018_simple.csv", "r")
# open_file2 = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

# csv_file2 = csv.reader(open_file2, delimiter=",")

header_row = next(csv_file)
name_index = header_row.index("NAME")
date_index = header_row.index("DATE")
high_index = header_row.index("TMAX")
low_index = header_row.index("TMIN")


# the enumerated() function returns both the index of each item and the value of each item
# as you loop through the list
# zero based index meaning first thing is 0


highs = []
dates = []
lows = []

# as an example
# somedate = '2018-07-01'
# converted_date = datetime.strptime(somedate, "%y-%m-%d")

for row in csv_file:
    try:
        high = int(row[high_index])
        low = int(row[low_index])
        converted_date = datetime.strptime(row[date_index], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {converted_date}")
    else:  ## for this I relpalces the hard keyed indexes into the thing
        highs.append(high)
        lows.append(low)
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


fig, ax = plt.subplots(2, 2)


# matplotlib's pyplot API has a convenienve function called subplots(
# utiil)
# enclosing figure object, in a single cell

fig2, ax = plt.subplots(2, 2)  # i took out 0 and 1 and replaced with high/low _index
a[high_index].plot(dates, highs, c="red")
a[low_index].plot(dates, lows, c="blue")

plt.show()