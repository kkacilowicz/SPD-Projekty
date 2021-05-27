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
    original = copy.deepcopy(Nset)
    NSet = copy.deepcopy(Nset)

    opty_harmonogram = []

    [Harmonogram, U] = schrage.Schrage(Nset)

    if U < UB:
        UB = U
        opty_harmonogram = Harmonogram

    [a, b, c] = blok.blok(Harmonogram, U)

    if c == -1:
        # for i in opty_harmonogram:
        #     print(i)
        print(str(U))
        return opty_harmonogram, U

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

        LB = schrageDistribution.SchrageWithDistributuion(NSetR2)

        if LB < UB:

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

Calier(Nset)

