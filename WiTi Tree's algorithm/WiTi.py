import csv

from Task import Task, punishment


def WiTi(tasks):

    # Number of OptimalPunishments is 2^n, where n is number of tasks
    # pow(2, len(task)) f. ex. if theres 3 tasks looks like that 00001000
    NumberOfCombinations = pow(2, len(tasks))

    # This variable is just to initialize array with random values
    # (in C++ we would do int tab = new int[NumberOfCombinations])
    n = 123456
    # In this array we store values of punishment of each iteration
    OptimalPunishments = [n] * NumberOfCombinations
    # We never use OptimalPunishments of 0
    OptimalPunishments[0] = 0

    # for each combination
    for i in range(1, NumberOfCombinations):
        # End of execution time of that task
        EndOfExecution = 0
        # Just a big value so as the algorithm works fine
        OptimalPunishments[i] = 10000000

        # Compute Cmax for this combination
        for j in range(0, len(tasks)):
            # If task is within this combination
            # Exactly, check if j bit within i is set
            # f ex if is 00001010 then it is true
            if i & (1 << j):
                # Add time of execution to Cmax
                EndOfExecution += tasks[j].p

        # Compute punishments
        for j in range(0, len(tasks)):
            # If task is within this combination
            if i & (1 << j):
                # Bit operator ~ means NOT
                # Check OPT for combination without this task and add punishment
                tmp = OptimalPunishments[i & (~(1 << j))] + punishment(tasks[j], EndOfExecution)
                # If it's smallest, then it is optimal
                OptimalPunishments[i] = min(OptimalPunishments[i], tmp)

    # return Optimal value for execution of all tasks
    return OptimalPunishments[NumberOfCombinations - 1]


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

result = WiTi(Tasks)
print(result)
