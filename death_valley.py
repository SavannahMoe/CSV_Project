# 1change to death valley file
#

import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

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
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {converted_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)


print(highs)

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
