import matplotlib.pyplot as plt
import random

random.seed(0)

fig = plt.figure(figsize=(50,30))

subplot = fig.add_subplot(1, 2, 1)


N = 100

boxdata1 = [random.randint(0, 20) for i in range(10)]
boxdata2 = [random.randint(20,40) for i in range(10)]
boxdata3 = [random.randint(40,60) for i in range(10)]
data = [boxdata1, boxdata2, boxdata3]
subplot.boxplot(data, vert=1)

plt.legend(loc='upper left', ncol = 4)
plt.savefig('boxPlots.png', format='png')
