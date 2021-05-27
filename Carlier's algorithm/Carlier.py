# Name: Carlier's algorithm
# Authors: Kacper Kaciłowicz 248951, Weronika Jakubowska 248931
# Date: 23.05.2021

import Schrage as schrage
import SchrageWithDistribution as schrageDistribution
import blok
import readFile
import copy
import math


def Calier(Nset):
    global UB
    global opty_harmonogram

    original = copy.deepcopy(Nset)
    NSet = copy.deepcopy(Nset)

    [Harmonogram, U] = schrage.Schrage(Nset)  # Schrage's algorithm determines the harmonogram and Cmax

    if U < UB: # update of the best solution
        UB = U
        opty_harmonogram = Harmonogram

    [a, b, c] = blok.blok(Harmonogram, U)  # determining the position of the task a, b, b

    if c == -1:   # if c doesn' t exist, the Schrage algorithm found an optimal solution
        return opty_harmonogram, UB

    else:
        if c + 1 >= len(opty_harmonogram): # if task c is the last one, r p q doesn't exist
            return None
        elif c + 1 == b:  # one element between c and b
            r = Harmonogram[c + 1].r
            q = Harmonogram[c + 1].q
            p = Harmonogram[c + 1].p
        else:
            r = min(Harmonogram[c + 1:b + 1]).r # r is the smallest r of the task at position c + 1 to b
            q = min(Harmonogram[c + 1:b + 1]).q # q is the smallest q of the task at position c + 1 to b
            p = 0                               # p is the sum of all p in positions c + 1 to b
            for i in range(c + 1, b + 1):
                p = p + Harmonogram[i].p

        index = 0
        for i in range(0, int(n)):
            if NSet[i].p == Harmonogram[c].p and NSet[i].q == Harmonogram[c].q:
                index = i
                NSet[i].r = max(Harmonogram[c].r, r + p) #  r (time of accessibility) is modified (task c is forced to run after
                                                         # all tasks in positions c +1 to b),

        NSetR2 = copy.deepcopy(NSet)
        NSetR3 = copy.deepcopy(NSet)

        LB_R = schrageDistribution.SchrageWithDistributuion(NSetR2) # Schrage's algorithm with distrubutuion determines lower bound

        if LB_R < UB:
            Calier(NSetR3)

        NSet[index].r = original[index].r #  r (time of accessibility) is modified to original values

        indexq = 0

        for i in range(0, int(n)):
            if NSet[i].p == Harmonogram[c].p and NSet[i].r == Harmonogram[c].r:
                indexq = i
                NSet[i].q = max(Harmonogram[c].q, q + p)  #  q ( time of deliver the task) is modified (task c is forced to run before
                                                         #  all tasks in positions c +1 to b),

        NSetQ1 = copy.deepcopy(NSet)
        NSetQ2 = copy.deepcopy(NSet)

        LB = schrageDistribution.SchrageWithDistributuion(NSetQ1) # Schrage's algorithm with distrubutuion determines lower bound

        if LB < UB:
            Calier(NSetQ2)

        NSet[indexq].q = original[indexq].q    #   q ( time of deliver the task) is modified to original values



filename = "SCHRAGE3.DAT"
[Nset, n] = readFile.readFile(filename)

UB = math.inf
opty_harmonogram = []
Calier(Nset)
print("Cmax : ", UB)
