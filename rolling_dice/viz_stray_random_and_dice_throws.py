import matplotlib.pyplot as plt
from plotly.graph_objs import Scatter, Layout
from plotly import offline

from die import Die
from random_walk import RandomWalk

# Utworzenie instancji klasy Die.
die_1 = Die()
die_2 = Die()

# Wykonanie rzutów kośćmi i przechowywanie wyników.
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Przygotowanie danych do wizualizacji rzutów kośćmi.
max_result = die_1.num_sides + die_2.num_sides
x_values = list(range(2, max_result+1))
frequencies = [results.count(value) for value in x_values]

# Utworzenie wykresu dla rzutów kośćmi.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(x_values, frequencies)

# Dodanie opisu wykresu i osi.
ax.set_title("Wynik rzucania dwiema kośćmi D6 tysiąc razy")
ax.set_xlabel('Wynik')
ax.set_ylabel('Częstotliwość występowania wartości')

# Wyświetlenie wykresu rzutów kośćmi.
plt.show()

# Przygotowanie danych do błądzenia losowego na podstawie rzutów kośćmi.
rw = RandomWalk(1000)
rw.fill_walk()

# Przygotowanie danych do wizualizacji błądzenia losowego.
data = [Scatter(x=rw.x_values, y=rw.y_values, mode='markers',
                marker=dict(size=3, color=rw.y_values, colorscale='Blues',
                            opacity=0.8))]

# Utworzenie układu wizualizacji błądzenia losowego.
layout = Layout(title='Błądzenie losowe na podstawie rzutu kośćmi',
                xaxis=dict(title='Krok'), 
                yaxis=dict(title='Wartość'))

# Zapisanie wizualizacji błądzenia losowego do pliku HTML.
offline.plot({'data': data, 'layout': layout}, filename='die_random_walk.html')

