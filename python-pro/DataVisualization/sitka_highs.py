import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    # Get high temperatures from this file.
    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)

print(highs)
print(dates)
# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()
plt.show()
first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(first_date)