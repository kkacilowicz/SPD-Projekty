# Name: Carlier algorithm
# Authors: Kacper Kaciłowicz 248951, Weronika Jakubowska 248931
# Date: 23.05.2021

import Schrage as schrage
import SchrageWithDistribution as schrageDistribution
import blok
import readFile
import copy
import math



def Calier(Nset, UB):
    NSetD = copy.deepcopy(Nset)
    NSet = copy.deepcopy(Nset)
    opty_harmonogram = []

    [Harmonogram, U] = schrage.Schrage(Nset)
    # NSetD = copy.deepcopy(Nset)
    # NSet = copy.deepcopy(Nset)
    # print(" na poczatku : U " + str(U) + " UB " + str(UB))

    if U < UB:
        UB = U
        opty_harmonogram = Harmonogram

    [a, b, c] = blok.blok(Harmonogram, U)

    if c == -1:
        print(" w if : U " + str(U) + " UB " + str(UB))
        return opty_harmonogram, U

    else:
        r = min(Harmonogram[c+1:b+1]).r
        q = min(Harmonogram[c+1:b+1]).q
        p = 0
        for i in range(c+1, b+1):
            p = p + Harmonogram[i].p

        Harmonogram_c_r = 0

        for i in range(0, int(n)):
            if NSetD[i].p == Harmonogram[c].p and NSetD[i].q == Harmonogram[c].q:
                Harmonogram_c_r = copy.copy(NSetD[i].r)
                NSetD[i].r = max(Harmonogram[c].r, r + p)

        NSetD2 = copy.deepcopy(NSetD)

        LB = schrageDistribution.SchrageWithDistributuion(NSetD)

        if LB < UB:
            print("Funkcja 1 U: ", U, " UB: ", UB)
            Calier(NSetD2, UB)

        # Harmonogram[c].r = Harmonogram_c_r

        Harmonogram_c_q = copy.copy(Harmonogram[c].q)

        for i in range(0, int(n)):
            if NSet[i].p == Harmonogram[c].p and NSet[i].r == Harmonogram[c].r:
                NSet[i].q = max(Harmonogram[c].q, q + p)

        NSet1 = copy.deepcopy(NSet)

        LB = schrageDistribution.SchrageWithDistributuion(NSet)
        if LB < UB:
            print("Funkcja 2 U: ", U, " UB: ", UB)
            Calier(NSet1, UB)

        # Harmonogram[c].q = Harmonogram_c_q



Nset=[]
filename = "SCHRAGE3.DAT"
[Nset, n] = readFile.readFile(filename)

UB = math.inf

x = Calier(Nset, UB)
print("efekt: ", x)




