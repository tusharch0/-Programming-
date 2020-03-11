import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [3, 9, 11, 2, 6]
plt.bar(x, y, label='Bars')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Graph1')
plt.legend()
plt.show()
