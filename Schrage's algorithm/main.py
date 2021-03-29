# Name: Schrage's algorithm program
# Authors: Kacper Kaciłowicz 248951, Weronika Jakubowska 248931
# Date: 29.03.2021

import csv

file = open("SCHRAGE1.DAT", "r")

# n - nb of tasks
# r - time of accessibility
# p - time of execution
# q - time of deliver the task
n = 0

# First elements of these lists will never be used - they're filled for better readability (problem with indexes)
r = [0]
p = [0]
q = [0]

if file.readable():
    n = file.readline()
    column = csv.reader(file, delimiter=' ')
    for row in column:
        r.append(row[0])
        p.append(row[1])
        q.append(row[2])
    file.close()

print(r)
print(p)
print(q)

