import csv

import matplotlib.pyplot as plt

filename ='data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	#Pobieranie temperatur maksymalnych z pliku.
	highs = []
	for row in reader:
		high = int(row[5])
		highs.append(high)

#Dane wykresu.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

#Formatowanie wykresu.
ax.set_title("Najwyższa temeperatura dnia, lipiec 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()