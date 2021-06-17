# Name: Schrage's algorithm program
# Authors: Kacper Kaciłowicz 248951, Weronika Jakubowska 248931
# Date: 17.06.2021
import copy

from Task import Task
from FinishTimeTask import FinishTimeTask

import csv


# Calculate Cmax of permutation
def CalculateCmax(Tasks):
    NbOfTasks = len(Tasks)
    NbOfMachines = len(Tasks[0].TimesOfExecution)

    # Created list of FinishTimeTask to store times of Finish of each task
    FinishTimes = []
    tmp = []
    # A list initialized with 0s
    for i in range(0, NbOfTasks):
        for j in range(0, NbOfMachines):
            tmp.append(0)
        FinishTimes.append(FinishTimeTask(tmp))
        tmp.clear()

    # Loop over tasks and machines
    for i in range(0, NbOfTasks):
        for j in range(0, NbOfMachines):

            # Time of finish of first task on first machine equals its time of execution
            if j == 0 and i == 0:
                FinishTimes[i].TimesOfFinish[j] = Tasks[i].TimesOfExecution[j]
            # First machine of task
            # Time of finish = Exectime + time when the machine is free
            elif j == 0:
                FinishTimes[i].TimesOfFinish[j] = Tasks[i].TimesOfExecution[j] + FinishTimes[i - 1].TimesOfFinish[j]
            # For first task
            # All machines are free so just add time of finish of previous task
            elif i == 0:
                FinishTimes[i].TimesOfFinish[j] = Tasks[i].TimesOfExecution[j] + FinishTimes[i].TimesOfFinish[j - 1]
            # In regular cases
            else:
                # Finish Time = Exec Time + Highest of when machine is free or when finished previous task
                FinishTimes[i].TimesOfFinish[j] = Tasks[i].TimesOfExecution[j] + \
                                                  max(FinishTimes[i].TimesOfFinish[j - 1],
                                                      FinishTimes[i - 1].TimesOfFinish[j])

    # Return Cmax
    return FinishTimes[NbOfTasks - 1].TimesOfFinish[NbOfMachines - 1]

# Compute best Cmax and permutation
def ComputePermutations(Tasks, ConsideredTask):

    # Cmax just a large number for algorithm
    Cmax = 1000000
    NbOfTasks = len(Tasks)

    # For each possible position of Considered task
    for i in range(0, NbOfTasks + 1):
        # Copy original to variable
        CopyOfInput = copy.deepcopy(Tasks)
        # Insert considered task on position
        CopyOfInput.insert(i, ConsideredTask)

        # Compute Cmax for this permutation
        c = CalculateCmax(CopyOfInput)
        # If it's better (smaller) then it's new Cmax
        if c < Cmax:
            Cmax = c
            # Save best permutation
            Result = copy.deepcopy(CopyOfInput)

    return Cmax, Result

# Main function for NEH's algorithm
def NEH(Tasks):
    Cmax = 0
    # List to store best possible permutation
    BestPermutation = []
    FirstIndex = 0
    # Get task with largest sum of execution times
    task = copy.deepcopy(Tasks[FirstIndex])
    # Remove it from list of tasks yet to be considered
    Tasks.pop(FirstIndex)
    # Add to Best Permutation list
    BestPermutation.append(task)
    NbOfTasks = len(Tasks)

    while NbOfTasks > 0:
        FirstIndex = 0
        # Get task with highest sum of exec times
        task = copy.deepcopy(Tasks[FirstIndex])
        # Remove it from list of tasks yet to be considered
        Tasks.pop(FirstIndex)
        # Compute result for actual set of tasks
        Cmax, Result = ComputePermutations(BestPermutation, task)
        # Save Best permutation
        BestPermutation = copy.deepcopy(Result)
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
