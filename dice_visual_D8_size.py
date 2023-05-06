from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Utworzoenie dwóch kości typu D8
die_1 = Die(8)
die_2 = Die(8)

#Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_num in range(10_000_000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#Analiza wyników:
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Wizualizacja wyników.

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_config = {'title': "Częstotliwość występowania wartości"}
my_layout = Layout(title='Wynik rzucania dwoma kośćmi D8 dzięsięć milionów razy',
	xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')