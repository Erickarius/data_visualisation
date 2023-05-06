from die import Die

#Utworzoenie kości typu D6
die = Die()

#Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

#Analiza wyników:
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

print(frequencies)