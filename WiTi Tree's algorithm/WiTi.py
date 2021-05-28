import csv

from Task import Task


# It's a list for unordered tasks (not ready to be executed)
Tasks = []

# Reeading from file and storing data in the list of NsetTasks
file = open("WiTi1.txt", "r")

if file.readable():
    n = file.readline()
    column = csv.reader(file, delimiter=' ')
    for row in column:
        # Filling a list with Task objects in format Task(p,w,d)
        Tasks.append(Task(row[0], row[1], row[2]))
    file.close()

for s in Tasks:
    print(s)

