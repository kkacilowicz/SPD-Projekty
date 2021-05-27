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

    [Harmonogram, U] = schrage.Schrage(Nset)

    if U < UB:
        UB = U
        opty_harmonogram = Harmonogram

    [a, b, c] = blok.blok(Harmonogram, U)


    if c == -1:
        return opty_harmonogram, UB

    else:
        if c + 1 >= len(opty_harmonogram):
            return None
        elif c + 1 == b:
            r = Harmonogram[c + 1].r
            q = Harmonogram[c + 1].q
            p = Harmonogram[c + 1].p
        else:
            r = min(Harmonogram[c + 1:b + 1]).r
            q = min(Harmonogram[c + 1:b + 1]).q
            p = 0
            for i in range(c + 1, b + 1):
                p = p + Harmonogram[i].p

        index = 0
        for i in range(0, int(n)):
            if NSet[i].p == Harmonogram[c].p and NSet[i].q == Harmonogram[c].q:
                index = i
                NSet[i].r = max(Harmonogram[c].r, r + p)

        NSetR2 = copy.deepcopy(NSet)
        NSetR3 = copy.deepcopy(NSet)

        LB_R = schrageDistribution.SchrageWithDistributuion(NSetR2)

        if LB_R < UB:
            Calier(NSetR3)

        NSet[index].r = original[index].r

        indexq = 0

        for i in range(0, int(n)):
            if NSet[i].p == Harmonogram[c].p and NSet[i].r == Harmonogram[c].r:
                indexq = i
                NSet[i].q = max(Harmonogram[c].q, q + p)

        NSetQ1 = copy.deepcopy(NSet)
        NSetQ2 = copy.deepcopy(NSet)

        LB = schrageDistribution.SchrageWithDistributuion(NSetQ1)

        if LB < UB:
            Calier(NSetQ2)

        NSet[indexq].q = original[indexq].q




filename = "SCHRAGE3.DAT"
[Nset, n] = readFile.readFile(filename)

UB = math.inf
opty_harmonogram = []
Calier(Nset)
print("Cmax : ", UB)

