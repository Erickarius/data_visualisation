import matplotlib.pyplot as plt

plt.style.use('seaborn')

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

#Zdefiniowanie tytułu wykresu i etykiet osi.
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartośc", fontsize=14)
ax.set_ylabel("Kwadrat wartości", fontsize=14)

#Zdefiniowanie wielkości etykiet.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()