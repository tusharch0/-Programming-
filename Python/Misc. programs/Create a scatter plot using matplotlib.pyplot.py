import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 9, 6, 12, 5, 1, 10, 5, 4, 9]

plt.scatter(x, y, label='scplots', color='r', s=60, marker="X")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.legend()
plt.show()
