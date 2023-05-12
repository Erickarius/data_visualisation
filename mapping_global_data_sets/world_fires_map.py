import json
import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Analiza struktury danych.
filename = 'data/world_fires_1_day.csv'

mags, lons, lats, hover_texts = [], [], [], []

with open(filename, 'r') as f:
    all_fires_data = csv.DictReader(f)

    for fire_dict in all_fires_data:
        mags.append(float(fire_dict['brightness']))
        lons.append(float(fire_dict['longitude']))
        lats.append(float(fire_dict['latitude']))
        hover_texts.append(fire_dict['acq_date'])

title = 'Mapa światowych pożarów'

data = [
    {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            'size': 5,
            'color': mags,
            'colorscale': 'Hot',
            'reversescale': True,
            'colorbar': {'title': 'Siła'},
        },
    }
]

my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fire_map.html')



