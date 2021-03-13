# n - nb of tasks
# r - time of accessibility
# p - time of execution

import csv

file = open("JACK8.DAT", "r")

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

# This is a declaration of list of tasks (list of tuples)
ListOfTasks = []

for i in range(1, int(n)+1):
    # Each task is a tuple with its r, p and i (i means ID of process)
    task = (int(r[i-1]), int(p[i-1]), i)
    # Add each task to List of tasks
    ListOfTasks.append(task)

# This is for better readability in next part of code
AccessIndex = 0
ExecIndex = 1

# List of C for each execution
# Initial condition is C(0) = r(0) + p(0)
C = [0]
# print(ListOfTasks)
for i in range(1, int(n)+1):
    # C is computed from the formula below and added to the list
    C_elem = max(int(ListOfTasks[i-1][AccessIndex]), C[i-1]) + int(ListOfTasks[i-1][ExecIndex])
    C.append(C_elem)

# C(0) doesn't need to be displayed (we're interested in 1,2,3...)
del C[0]

# Prints list of termination of each task
print("Termination of each task before they're sorted: ", C)

# Now we'll see how it works with r sorted in non-descending order
ListOfTasks.sort()
C.clear()

# List of termination time for each execution
# Initial condition is C(0) = 0
C = [0]

for i in range(1, int(n)+1):
    # C is computed from the formula below and added to the list
    C_elem = max(int(ListOfTasks[i-1][AccessIndex]), C[i-1]) + int(ListOfTasks[i-1][ExecIndex])
    C.append(C_elem)

# Cmax is the termination time of final task
Cmax = C[int(n)]

# C(0) doesn't need to be displayed (we're interested in 1,2,3...)
del C[0]

# Prints list of termination of each task
print("Termination of each task after they're sorted: ", C)

# Time of termination for the last task
print("Cmax: ", Cmax)



# Tu jest wszystko to co Werka probowala (może ja pojedyncze nazwy zmieniłem)

# C = [int(r[0])+int(p[0])]
# First_tuple = (int(r[0]),  C[0])
# list = []
# list.append(First_tuple)
#
# for i in range(1, int(n)):
#     C.append(max(int(r[i]), C[i-1]) + int(p[i]))
#     Next_tuple = (int(r[i]), C[i])
#     list.append(Next_tuple)
#
# print("C:", C)
# print("Lista: ", list)
# list.sort()
# print("Lista: ", list)
# Cmax = list[int(n)-1][1]
# print("Cmax ", Cmax)
#
