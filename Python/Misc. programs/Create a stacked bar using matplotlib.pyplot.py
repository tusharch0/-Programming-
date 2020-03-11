import matplotlib.pyplot as plt
import numpy as np

N = 6

y1 = [3, 9, 11, 2, 6, 4]

y2 = [6, 4, 7, 8, 3, 4]

xvalues = np.arange(N)

plt.bar(xvalues, y1, color='b', label='Team1')
plt.bar(xvalues, y2, color='r', bottom=y1, label='Team2')
plt.xticks(xvalues, ('V1', 'V2', 'V3', 'V4', 'V5'))

plt.xlabel('Teams')
plt.ylabel('Scores')
plt.title('Stacked Bar Graphs')
plt.legend()
