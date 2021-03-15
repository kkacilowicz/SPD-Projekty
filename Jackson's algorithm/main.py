# Name: Jackson's algorithm program
# Authors: Kacper Kaciłowicz 248951, Weronika Jakubowska 248931
# Date: 16.03.2021

import csv

file = open("JACK3.DAT", "r")

# n - nb of tasks
# r - time of accessibility
# p - time of execution
n = 0

# First elements of these lists will never be used - they're filled for better readability (problem with indexes)
r = [0]
p = [0]
if file.readable():
    n = file.readline()
    column = csv.reader(file, delimiter=' ')
    for row in column:
        r.append(row[0])
        p.append(row[1])
    file.close()

# This is a declaration of list of tasks (list of tuples) [First tuples are never used (indexes)]
ListOfTasks = [(0, 0)]

for i in range(1, int(n) + 1):
    # Each task is a tuple with its r, p and i (i means ID of process)
    task = (int(r[i]), int(p[i]))
    # Add each task to List of tasks
    ListOfTasks.append(task)

# This is for better readability in next part of code
AccessIndex = 0
ExecIndex = 1

# List of C for each execution
# Initial condition is C(0) = r(0) + p(0)
C = [0]
# print(ListOfTasks)
for i in range(1, int(n) + 1):
    # C is computed from the formula below and added to the list
    C_elem = max(int(ListOfTasks[i][AccessIndex]), C[i - 1]) + int(ListOfTasks[i][ExecIndex])
    C.append(C_elem)

# Cmax is the termination time of final task
Cmax = C[int(n)]

print("Cmax with tasks disordered: ", Cmax)

# Now we'll see how it works with r sorted in non-descending order
ListOfTasks.sort()
C.clear()

# List of termination time for each execution
# Initial condition is C(0) = 0
C = [0]

for i in range(1, int(n) + 1):
    # C is computed from the formula below and added to the list
    C_elem = max(int(ListOfTasks[i][AccessIndex]), C[i - 1]) + int(ListOfTasks[i][ExecIndex])
    C.append(C_elem)

# Cmax is the termination time of final task
Cmax = C[int(n)]

# Time of termination for the last task
print("Cmax with tasks ordered: ", Cmax)
