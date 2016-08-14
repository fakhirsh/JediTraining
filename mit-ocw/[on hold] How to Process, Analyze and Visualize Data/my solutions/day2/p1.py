import matplotlib.pyplot as plt
import random

random.seed(0)

fig = plt.figure(figsize=(50,30))

subplot = fig.add_subplot(2, 3, 1)


N = 100

xs = range(N)
y1 = [random.randint(0,50) for i in xs]
y2 = range(N)

subplot.bar(xs, y2, color='red', linewidth=0, label='ys') 
subplot.bar(xs, y1, linewidth=0) 

plt.legend(loc='upper left', ncol = 4)
plt.savefig('bar chart.png', format='png')
