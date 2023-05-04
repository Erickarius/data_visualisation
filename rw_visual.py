import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Przygotowaniedanych błądzenia losowego, dopóki program pozostaje aktywny

while True:
	#Przygotowanie danych błądzenia losowego i wyświetlanie punktów.
	rw = RandomWalk(5000)
	rw.fill_walk()

	#Wyświetlenie punktów błądzenia losowego.
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
	point_numbers = range(rw.num_points)

	ax.plot(rw.x_values, rw.y_values, linewidth=3)
	#ax.plot(0, 0, c="green", edgecolor='none', s=100)
	#ax.plot(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
	#	s=100)

	#Ukrycie osi.
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()
	keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
	if keep_running == 'n':
		break
