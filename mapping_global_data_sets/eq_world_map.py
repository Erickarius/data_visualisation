import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Analiza stuktury danych.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	mags.append(mag)
	lons.append(lon)
	lats.append(lat)

data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Trzęsienia ziemi na świecie')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')