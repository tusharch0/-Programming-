import matplotlib.pyplot as plt
x1 = [2, 4, 6, 8, 10]
y1 = [3, 9, 11, 2, 6]

x2 = [1, 3, 5, 7, 9]
y2 = [6, 4, 7, 8, 3]

plt.bar(x1, y1, label='Bars1', color='g')
plt.bar(x2, y2, label='Bars2', color='r')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Graph2')
plt.legend()
plt.show()
