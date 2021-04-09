# Name: Schrage's algorithm with distrubotion program
# Authors: Kacper Kaciłowicz 248951, Weronika Jakubowska 248931
# Date: 09.04.2021

import csv
import heapq


# Class which contains info about each task
class Task:
    # Constructor of class
    def __init__(self, r, p, q):
        # r - time of accessibility
        # p - time of execution
        # q - time of deliver the task
        self.r = int(r)
        self.p = int(p)
        self.q = int(q)

    # This is a definition used in printing an object
    def __str__(self):
        return "r: %d p: %d q: %d" % (self.r, self.p, self.q)


# Class for unordered tasks - they are sorted differently than the ordered ones
class NsetTask(Task):
    def __init__(self, r, p, q):
        super().__init__(r, p, q)

    # Operator Less Than overloaded
    def __lt__(self, other):
        self_r = self.r
        other_r = other.r
        return self_r < other_r


# Class for unordered tasks - they are sorted differently than the ordered ones
class GsetTask(Task):
    def __init__(self, othertask):
        super().__init__(othertask.r, othertask.p, othertask.q)

    # Operator Less Than overloaded
    def __lt__(self, other):
        self_q = self.q
        other_q = other.q
        return self_q < other_q


# n - nb of tasks
n = 0
# It's a list for unordered tasks (not ready to be executed)
NSet = []

# Reading from file and storing data in the list of NsetTasks
file = open("SCHRAGE9.DAT", "r")

if file.readable():
    n = file.readline()
    column = csv.reader(file, delimiter=' ')
    for row in column:
        # Filling a list with Task objects in format Task(r,p,q)
        NSet.append(NsetTask(row[0], row[1], row[2]))
    file.close()


# Tasks are sorted in ascending order (With ascending value of NsetTask obj.r)
NSet.sort()

# Variables initialized (t - actual moment in time, Cmax - Max time of delivery,
t = 0
Cmax = 0

# It's a list of tasks ready to be executed
# It stores GsetTask objects which are sorted in descending order (With descending value of obj.q)
GSet = []

# l is an actual processed task (q is very big so as not to mess with first execution of a loop)
l = Task(0, 0, 10000000000)
k = 0
# While lists are not empty
while len(NSet) != 0 or len(GSet) != 0:
    # While smallest time of accessibility is smaller than actual moment in time (and Nset is not empty)
    while len(NSet) != 0 and min(NSet).r <= t:
        # Task with smallest r is removed from NSet and added to variable e
        # heapq library makes a list behave like a heap, where Nset is a min-heap, Gset is a max-heap
        e = heapq.heappop(NSet)
        # e is appended to list, from now on NsetTask became GsetTask
        GSet.append(GsetTask(e))

        # If time of delivery of considered task is higher than the one of actual task
        if e.q > l.q:
            # Stop executing l task
            l.p = t - e.r
            t = e.r
            if l.p > 0:
                # Add task with time left to be executed
                GSet.append(GsetTask(l))
        # Apparently you always have to heapify (make heap out of list) when you have populated list
        # Otherwise algorithm doesn't work
        heapq._heapify_max(GSet)

    # In a situation where Gset is empty, t = smallest r in Nset
    if len(GSet) == 0:
        t = min(NSet).r
    else:
        # e = GsetTask with highest q
        e = heapq._heappop_max(GSet)
        # Actual task is now e
        l = e
        # Actual moment in time = Previous moment in time + time of execution of this task
        t = t + e.p
        # Max time of delivery = Hiqhest of old Cmax vs actual time + time of delivery
        Cmax = max(Cmax, t + e.q)


print("Cmax: ", Cmax)
