import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Przygotowaniedanych błądzenia losowego, dopóki program pozostaje aktywny

while True:
	#Przygotowanie danych błądzenia losowego.
	rw = RandomWalk()
	rw.fill_walk()

	#Wyświetlenie punktów błądzenia losowego.
	plt.style.use('classic')
	fig, ax = plt.subplots()
	ax.scatter(rw.x_values, rw.y_values, s=15)
	plt.show()
	keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
	if keep_running == 'n':
		break
