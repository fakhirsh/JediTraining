import sys

csvFile = open(sys.argv[1],'r')

count = 0
for line in csvFile:
    # Print the header first
    if count == 0:
        print(line[:-1])        
    if "OBAMA" in line.upper() or "MCCAIN" in line.upper():
        print(line[:-1])
    count += 1
