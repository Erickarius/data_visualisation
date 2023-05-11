import json
import codecs
import numpy as np

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Analiza struktury danych.
filename = 'data/eq_data_7_day.json'
with codecs.open(filename, 'r', encoding='utf-8-sig') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    if mag is not None:  # Sprawdzenie, czy wartość mag istnieje
        mag = float(mag)
        mag = max(mag, 0)  # Ograniczenie wartości do nieujemnych liczb
        mags.append(mag)
        lons.append(eq_dict['geometry']['coordinates'][0])
        lats.append(eq_dict['geometry']['coordinates'][1])
        hover_texts.append(eq_dict['properties']['title'])

title = all_eq_data['metadata']['title']

data = [
    {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            'size': [5 * mag for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Siła'},
        },
    }
]

my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_7_day.html')
