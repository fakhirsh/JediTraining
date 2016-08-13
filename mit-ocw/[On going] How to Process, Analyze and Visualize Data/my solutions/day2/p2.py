import matplotlib.pyplot as plt
import random

random.seed(0)

fig = plt.figure(figsize=(50,30))

subplot = fig.add_subplot(2, 3, 1)


N = 100

xs = range(N)
y1 = [random.randint(0,50) for i in xs]
y2 = range(N)

subplot.plot(xs, y2, color='red', label='y2') 
subplot.plot(xs, y1, label='y1') 

plt.legend(loc='upper left', ncol = 4)
plt.savefig('line chart.png', format='png')
