# n - nb of tasks
# r - time of accessibility
# p - time of execution

import csv

file = open("JACK2.DAT", "r")

n = 0
r = []
p = []
if file.readable():
    n = file.readline()
    column = csv.reader(file, delimiter=' ')
    for row in column:
        r.append(row[0])
        p.append(row[1])
    file.close()

print("Data:")
print("n: ", n, end="")
print("r: ", r)
print("p: ", p)

C = [int(r[0])+int(p[0])]

for i in range(1, int(n)):
   C.append(max(int(r[i]), C[i-1])+int(p[i]))

print(C)


r.sort()
print("r:", r)
C.clear()
C = [int(r[0])+int(p[0])]
for i in range(1, int(n)):
   C.append(max(int(r[i]), C[i-1])+int(p[i]))

print(C)