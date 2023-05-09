import json

#Analiza stuktury danych.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)
	readalbe_file = 'data/readable_eq_data.json'
	with open(readalbe_file, 'w') as f:
		json.dump(all_eq_data, f, indent=4)