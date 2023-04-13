import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'data/sitka_weather_07-2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

    # Чтение максимальных температур и дат из файла.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Нанесение данных на диаграмму.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Форматирование диаграммы.
plt.title("Daily high trmperatures, July 2021", fontsize=24)
plt.xlabel('', fontsize=16)

plt.show()
