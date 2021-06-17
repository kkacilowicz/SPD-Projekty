# Name: Schrage's algorithm program
# Authors: Kacper Kaciłowicz 248951, Weronika Jakubowska 248931
# Date: 17.06.2021
import copy

from Task import Task
from FinishTimeTask import FinishTimeTask

import csv


# //liczy cmax permutacji
def CalculateCmax(Tasks):
    # //sprawdż wielkość danych
    n = len(Tasks)
    m = len(Tasks[0].TimesOfExecution)

    FinishTimes = []
    tmp = []
    for i in range(0, n):
        for j in range(0, m):
            tmp.append(0)
        FinishTimes.append(FinishTimeTask(tmp))
        tmp.clear()

    # //iterując kolejno po zadaniach i maszynach zadania
    for i in range(0, n):
        for j in range(0, m):

            if j == 0 and i == 0:
                # //pierwsze pole
                FinishTimes[i].TimesOfFinish[j] = Tasks[i].TimesOfExecution[j]
            elif j == 0:
                # //pierwsza kolumna
                FinishTimes[i].TimesOfFinish[j] = Tasks[i].TimesOfExecution[j] + FinishTimes[i - 1].TimesOfFinish[j]
                # //czas 1 maszyny + termin zakonczenia zadania wczesniej na maszynie 1
            elif i == 0:
                FinishTimes[i].TimesOfFinish[j] = Tasks[i].TimesOfExecution[j] + FinishTimes[i].TimesOfFinish[j - 1]
                # //dodaj czas wykonywania + czas wyjscia z maszyny

            else:

                if FinishTimes[i].TimesOfFinish[j - 1] > FinishTimes[i - 1].TimesOfFinish[j]:
                    # //poównanie czasu skonczenia obecnej maszyny i poprzedniego zadania
                    FinishTimes[i].TimesOfFinish[j] = Tasks[i].TimesOfExecution[j] + FinishTimes[i].TimesOfFinish[j - 1]
                else:
                    FinishTimes[i].TimesOfFinish[j] = Tasks[i].TimesOfExecution[j] + FinishTimes[i - 1].TimesOfFinish[j]

    return FinishTimes[n - 1].TimesOfFinish[m - 1]


def ComputePermutations(Tasks, ConsideredTask):
    Cmax = 1000000
    n = len(Tasks)

    for i in range(0, n + 1):
        CopyOfInput = copy.deepcopy(Tasks)
        CopyOfInput.insert(i, ConsideredTask)

        c = CalculateCmax(CopyOfInput)
        if c < Cmax:
            Cmax = c
            Result = copy.deepcopy(CopyOfInput)

    return Cmax, Result


def NEH(Tasks):
    Cmax = 0
    best_permutation = []
    FirstIndex = 0
    task = copy.deepcopy(Tasks[FirstIndex])
    Tasks.pop(FirstIndex)
    best_permutation.append(task)
    NbOfTasks = len(Tasks)

    while  NbOfTasks > 0:
        FirstIndex = 0
        task = copy.deepcopy(Tasks[FirstIndex])
        Tasks.pop(FirstIndex)

        Cmax, Result = ComputePermutations(best_permutation, task)
        best_permutation = copy.deepcopy(Result)
        NbOfTasks = NbOfTasks - 1

    return Cmax


Tasks = []
NbOfTasks = 0
NbOfMachines = 0

# Reading from file and storing data in the list of NsetTasks
file = open("NEH2.DAT", "r")

if file.readable():
    linecount = 0
    column = csv.reader(file, delimiter=' ')
    for row in column:
        if linecount == 0:
            NbOfTasks = row[0]
            NbOfMachines = row[1]
        else:
            # Filling a list with Task objects in format Task(TimeOfExecution)
            Tasks.append(Task(row, linecount))
        linecount += 1
    file.close()

SortedTasks = sorted(Tasks, key=lambda x: x.SumOfTimes, reverse=True)

print(NEH(SortedTasks))
