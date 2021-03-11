# n - nb of tasks
# r - time of accessibility
# p - time of execution

import csv

file = open("JACK8.DAT", "r")

n = 0
r = 0
p = 0
if file.readable():
    n = file.readline()
    column = csv.reader(file, delimiter=' ')
    r = []
    p = []
    for row in column:
        r.append(row[0])
        p.append(row[1])
    file.close()

print("Data:")
print("n: ", n, end="")
print("r: ", r)
print("p: ", p)
