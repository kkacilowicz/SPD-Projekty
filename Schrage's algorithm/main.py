# Name: Schrage's algorithm program
# Authors: Kacper Kaciłowicz 248951, Weronika Jakubowska 248931
# Date: 07.04.2021

import csv
import heapq


# Class which contains info about each task
class Task:
    # Constructor of class
    def __init__(self, r, p, q):
        # r - time of accessibility
        # p - time of execution
        # q - time of deliver the task
        self.r = r
        self.p = p
        self.q = q

    # This is a definition used in printing an object
    def __str__(self):
        return "r: %d p: %d q: %d" % (self.r, self.p, self.q)


class NsetTask(Task):
    def __init__(self, r, p, q):
        super().__init__(r, p, q)

    # Operator Less Than overloaded
    def __lt__(self, other):
        self_r = self.r
        other_r = other.r
        return self_r < other_r


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


# It's a list for unordered tasks
NSet = []

file = open("SCHRAGE1.DAT", "r")

if file.readable():
    n = file.readline()
    column = csv.reader(file, delimiter=' ')
    for row in column:
        # Filling a list with Task objects in format Task(r,p,q)
        NSet.append(NsetTask(row[0], row[1], row[2]))
    file.close()

for obj in NSet:
    print(obj.r, obj.p, obj.q)

print("sortowanie")
NSet.sort()


for obj in NSet:
    print(obj.r, obj.p, obj.q)


# Do GSet będę chciał używać heapq itd, do Nset nie jest potrzebny

t = 0
k = 0
Cmax = 0
G = []
N = []
#
# for i in range(1, int(n) + 1):
#     N.append(i)
#
# print("N:", N)
#
# while len(G) != 0 or len(N) != 0:  # dopoki zbior G lub N nie sa puste
#     print("jestem w algorytmie")
#     while len(N) != 0 and min(r) <= t:
#         e = min(r)  # e to najmniejszy element r
#         if G.count(e) == 0:
#             G.append(e)  # tu taka ala suma zbioru
#         if N.count(e) != 0:
#             N.remove(e)  # tu różnica zbioru
#     if len(G) == 0:
#         t = min(r)
#         continue
#     e = max(q)
#     G.remove(e)
#     k = k + 1
#     t = t + p
#     Cmax = max(Cmax, t + q)
#
# print("poszło po ")
# print(Cmax)
