import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
slices = [7, 2, 2, 13]
cols = ['r', 'y', 'g', 'b']

my_labels = ["Sleeping ", "Eating", "Working", "Playing"]

plt.pie(slices,
        labels=my_labels,
        colors=cols,
        startangle=45,
        explode=(0, 0.2, 0, 0),
        shadow=True,
        autopct='%1.1f%%')
plt.axis('equal')
plt.legend(loc=3)
plt.show()
