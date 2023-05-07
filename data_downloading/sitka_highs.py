import csv

filename ='data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	#Pobieranie temperatur maksymalnych z pliku.
	highs = []
	for row in reader:
		high = int(row[5])
		highs.append(high)

print(highs)