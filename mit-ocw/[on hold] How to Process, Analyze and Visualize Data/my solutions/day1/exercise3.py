import csv, sys, datetime, time
import matplotlib.pyplot as plt
from collections import defaultdict, OrderedDict

time_start = time.time()

reader = csv.DictReader(open(sys.argv[1], 'r'))

candidateDict = defaultdict(lambda:0)

for row in reader:
    name = row["cand_nm"]
    amount = float(row["contb_receipt_amt"])
    if amount < 0:
        candidateDict[name] += amount
    
fig = plt.figure(figsize = (15,5))

xs = [k for k in candidateDict]
ys = [candidateDict[k] for k in candidateDict]

for k,v in candidateDict.items():
    print(k, "\t\t: ", v)

'''  
plt.plot(xs, ys, label="Sneaky")
plt.legend(loc="upper center", ncol = 4)

plt.savefig("exercise3.png", format="png")
'''
time_end = time.time()

print("Time Elapsed:", time_end - time_start)
