from die import Die

#Utworzoenie kości typu D6
die = Die()

#Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_num in range(100):
	result = die.roll()
	results.append(result)

print(results)