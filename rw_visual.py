import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Przygotowaniedanych błądzenia losowego, dopóki program pozostaje aktywny

while True:
	#Przygotowanie danych błądzenia losowego i wyświetlanie punktów.
	rw = RandomWalk()
	rw.fill_walk()

	#Wyświetlenie punktów błądzenia losowego.
	plt.style.use('classic')
	fig, ax = plt.subplots()
	point_numbers = range(rw.num_points)

	ax.scatter(rw.x_values, rw.y_values, c=point_numbers, 
		cmap=plt.cm.Blues, edgecolor='none', s=15)
	ax.scatter(0, 0, c="green", edgecolor='none', s=100)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
		s=100)

	plt.show()
	keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
	if keep_running == 'n':
		break
