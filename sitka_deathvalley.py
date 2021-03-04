# 1 changing file to include all data from 2018
# 2. change the title to daily high and low temperature -2018
# 3 extract low temps from file and add to the chart

import csv
from datetime import datetime

open_file1 = open("sitka_weather_2018_simple.csv", "r")
csv_file1 = csv.reader(open_file1, delimiter=",")

header_row = next(csv_file1)
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

for row in csv_file1:
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
title = row[name_index]
# death valley
open_file2 = open("death_valley_2018_simple.csv", "r")

csv_file2 = csv.reader(open_file2, delimiter=",")

header_row = next(csv_file2)
name_index = header_row.index("NAME")
date_index = header_row.index("DATE")
high_index = header_row.index("TMAX")
low_index = header_row.index("TMIN")

highs2 = []
dates2 = []
lows2 = []


for row in csv_file2:
    try:
        high = int(row[high_index])
        low = int(row[low_index])
        converted_date = datetime.strptime(row[date_index], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {converted_date}")
    else:  ## for this I relpalces the hard keyed indexes into the thing
        highs2.append(high)
        lows2.append(low)
        dates2.append(converted_date)
title2 = row[name_index]
# print(highs)

# plot highs on a chart


# matplotlib's pyplot API has a convenienve function called subplots(
# utiil)
# enclosing figure object, in a single cell

maintitle = "Temperature comparison between " + title + " and " + title2
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 1)
ax[0].plot(dates, highs, c="red")
ax[0].plot(dates, lows, c="blue")
ax[0].fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
ax[0].set_title(title, fontsize=16)
ax[0].tick_params(axis="both", labelsize=12)
ax[1].plot(dates2, highs2, c="red")
ax[1].plot(dates2, lows2, c="blue")
ax[1].fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)
ax[1].set_title(title2, fontsize=16)
ax[1].tick_params(axis="both", labelsize=12)
fig.autofmt_xdate()
fig.suptitle(maintitle, fontsize=16)

plt.show()