import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename ='data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	#Pobieranie dat oraz najwyższych i najniższych temperatur z pliku
	dates_1, highs_1, lows_1 = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], "%Y-%m-%d")
		high = int(row[5])
		low = int(row[6])
		dates_1.append(current_date)
		highs_1.append(high)
		lows_1.append(low)

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	#Pobieranie dat oraz najwyższych i najniższych temperatur z pliku
	dates_2, highs_2, lows_2 = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], "%Y-%m-%d")
		try:
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Brak danych dla {current_date}.")
		dates_2.append(current_date)
		highs_2.append(high)
		lows_2.append(low)

#Wygenerowanie wykresu najniższych i najwyżych temperatur.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates_1, highs_1, c='red', alpha=0.5)
ax.plot(dates_1, lows_1, c='blue', alpha=0.5)
ax.fill_between(dates_1, highs_1, lows_1, facecolor='blue', alpha=0.1)
ax.plot(dates_2, highs_2, c='black', alpha=0.5)
ax.plot(dates_2, lows_2, c='green', alpha=0.5)
ax.fill_between(dates_2, highs_2, lows_2, facecolor='green', alpha=0.1)

#Formatowanie wykresu.
ax.set_title("Najwyższa i najniższa temeperatura dnia - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()