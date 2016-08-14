import sys

csvFile = open(sys.argv[1],'r')

count = 0
for line in csvFile:
    if count % 1000 == 0:
        print(line[:-1])
    count += 1
