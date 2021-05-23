import csv
import Task

def readFile(filename):

    # n - nb of tasks
    n = 0
    # It's a list for unordered tasks (not ready to be executed)
    NSet = []

    # Reeading from file and storing data in the list of NsetTasks
    file = open(filename, "r")

    if file.readable():
        n = file.readline()
        column = csv.reader(file, delimiter=' ')
        for row in column:
            # Filling a list with Task objects in format Task(r,p,q)
            NSet.append(Task.NsetTask(row[0], row[1], row[2], 0))
        file.close()

    return NSet, n