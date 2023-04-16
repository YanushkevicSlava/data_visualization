import csv
from matplotlib import pyplot as plt
from datetime import datetime


file_name = 'data/MAGNOLIA.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, rainfalls = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        rainfall = row[3]
        dates.append(current_date)
        rainfalls.append(rainfall)

# Нанесение данных на диаграмму.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, c='red')

# Форматирование диаграммы.
plt.title("Rainfall in Magnolia in 2023", fontsize=24)

plt.show()
