# Name: Carlier algorithm
# Authors: Kacper Kaciłowicz 248951, Weronika Jakubowska 248931
# Date: 23.05.2021

import Schrage as schrage
import SchrageWithDistribution as schrageDistribution
import blok as blok
import readFile
import copy
import math

Nset=[]
filename = "SCHRAGE3.DAT"
[Nset, n] = readFile.readFile(filename)

UB = math.inf


def Calier(Nset, UB):
    NSetD = copy.deepcopy(Nset)
    NSet = copy.deepcopy(Nset)
    [Harmonogram, U] = schrage.Schrage(Nset)
    print("Nowe wywołanie U: ", U, " UB ", UB)
    if U < UB:
        UB = U
        # print("UB", UB, "U", U)
        opty_harmonogram = Harmonogram
    [a, b, c] = blok.blok(Harmonogram, U)
    if c == -1:
        print("C == -1")
        print("U", U, "UB", UB)
        return 0
    else:

        # print("a ", a," b ", b," c ", c)

        r = min(Harmonogram[c+1:b+1]).r
        q = min(Harmonogram[c+1:b+1]).q
        p = 0
        for i in range(c+1, b+1):
            p = p + Harmonogram[i].p

        # print("r", r, "q", q, "p", p)

        Harmonogram_c_r = copy.copy(Harmonogram[c].r)
        Harmonogram[c].r = max(Harmonogram[c].r, r + p)


        for i in range(0, int(n)):
            if NSetD[i].p == Harmonogram[c].p and NSetD[i].q == Harmonogram[c].q:
                NSetD[i].r = max(Harmonogram[c].r, r + p)
        NSetD2 = copy.deepcopy(NSetD)
        LB = schrageDistribution.SchrageWithDistributuion(NSetD)
        print("Dla R: LB: ", LB, "UB: ", UB)

        if LB < UB:
            Calier(NSetD2, UB)
        print("H", Harmonogram_c_r)
        Harmonogram[c].r = Harmonogram_c_r

        Harmonogram_c_q = copy.copy(Harmonogram[c].q)
        Harmonogram[c].q = max(Harmonogram[c].q, q + p)

        for i in range(0, int(n)):
            if NSet[i].p == Harmonogram[c].p and NSet[i].r == Harmonogram[c].r:
                NSet[i].r = max(Harmonogram[c].r, r + p)

        NSet1 = copy.deepcopy(NSet)
        # print("Dla q: LB: ", LB, "UB: ", UB)

        LB = schrageDistribution.SchrageWithDistributuion(NSet)
        if LB < UB:
            Calier(NSet1, UB)
        Harmonogram[c].q = Harmonogram_c_q


Calier(Nset, UB)





