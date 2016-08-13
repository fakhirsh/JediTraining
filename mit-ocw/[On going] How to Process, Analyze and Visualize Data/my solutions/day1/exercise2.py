import csv, sys, datetime, time
import matplotlib.pyplot as plt
from collections import defaultdict, OrderedDict

time_start = time.time()

reader = csv.DictReader(open(sys.argv[1], 'r'))

obamaDonations = defaultdict(lambda:0)
mccainDonations = defaultdict(lambda:0)

for row in reader:
    name = row["cand_nm"]
    amount = float(row["contb_receipt_amt"])
    datestr = row["contb_receipt_dt"]
    date = datetime.datetime.strptime(datestr, "%d-%b-%y")
    
    if "OBAMA" in name.upper():
        obamaDonations[date] += amount
        
    if "MCCAIN" in name.upper():
        mccainDonations[date] += amount

fig = plt.figure(figsize = (25,5))
        
obama_sorted = sorted(obamaDonations.items(), key=lambda x: x[0])
obama_OrdDic = OrderedDict(obama_sorted)
xs1 = [k for k in obama_OrdDic]
ysO = [obama_OrdDic[k] for k in obama_OrdDic]
ys1 = []
sum = 0
for i in range(len(ysO)):
    sum += ysO[i]
    ys1.append(sum)

mccain_sorted = sorted(mccainDonations.items(), key=lambda x: x[0])
mccain_OrdDic = OrderedDict(mccain_sorted)
xs2 = [k for k in mccain_OrdDic]
ysM = [mccain_OrdDic[k] for k in mccain_OrdDic]
ys2 = []
sum = 0
for i in range(len(ysM)):
    sum += ysM[i]
    ys2.append(sum)
    
    
plt.plot(xs1, ys1, label="Obama")
plt.plot(xs2, ys2, label="McCain")
plt.legend(loc="upper center", ncol = 4)

plt.savefig("exercise2.png", format="png")

time_end = time.time()

print("Time Elapsed:", time_end - time_start)
