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

# We make empty lists
r = []
p = []
q = []

if file.readable():
    n = file.readline()
    column = csv.reader(file, delimiter=' ')
    for row in column:
        r.append(int(row[0]))
        p.append(int(row[1]))
        q.append(int(row[2]))
    file.close()

print(r)
print(p)
print(q)

"""
t = 0
k = 0
Cmax = 0
G = {} # pusty zbior G
N = {1}
for i in range(1, int(n)+1):
    N.add(i)  # tworzenie zbioru N

while len(G) != 0 or len(N) != 0:  # dopoki zbior G lub N nie sa puste
   while len(N) != 0  and min(r) <= t:
        e = min(r) # e to najmniejszy element r
        G = G | set(e)  # | to suma
        N = N - set(e)  # - zwraca roznice zbiorow
   if len(G) == 0:
       t = min(r)
       continue
   e = max(q)
   G = G - e
   k=k+1
   t = t + p
   Cmax = max(Cmax, t + q)

print(Cmax)

"""