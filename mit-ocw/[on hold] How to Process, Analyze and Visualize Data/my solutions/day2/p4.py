import matplotlib.pyplot as plt
import random

random.seed(0)

fig = plt.figure(figsize=(10,6))

subplot = fig.add_subplot(1, 1, 1)


N = 100

xs = range(10000)
ys = [random.randint(0,40)*random.randint(0,40)*random.randint(0,40) for i in range(len(xs))]
subplot.scatter(xs, ys, s=20, c='red', linewidth=0)

plt.legend(loc='upper left', ncol = 4)
plt.savefig('scatterPlot.png', format='png')
