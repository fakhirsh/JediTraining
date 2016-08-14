
import random

xs = range(10)
#ys = [random.randint(0,20) for i in range(10)]
ys = [1 for i in range(10)]
#ys1 = [ys[i] + ys[i+1]  for i in range(0,len(ys))]

ys1 = []
sum = 0

for i in range(len(ys)):
    sum += ys[i]
    ys1.append(sum)

print(ys)
print(ys1)
