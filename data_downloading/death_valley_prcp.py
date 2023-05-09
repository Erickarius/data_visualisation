import csv

from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	#Pobieranie danych dotyczących opadów deszczu
	dates, rainfall = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], "%Y-%m-%d")
		rain = float(row[3]) * 100
		dates.append(current_date)
		rainfall.append(rain)

#Dane wykresu
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='blue')

#Formatowanie wykresu
ax.set_title("Procent opadów deszczu w 2018.r", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Procent opadów deszczu", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()