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
# Harmonogram = []
# [Harmonogram, U] = schrage.Schrage(Nset)

def Calier(Nset, UB):
    NSetD = copy.deepcopy(Nset)
    NSetD2 = copy.deepcopy(Nset)
    NSet = copy.deepcopy(Nset)
    NSet1 = copy.deepcopy(Nset)
    [Harmonogram, U] = schrage.Schrage(Nset)
    print("Wchodze ->   U : " + str(U) + " harmonogram : ")
    for i in Harmonogram:
        print(i)
    print("UB", UB)
    if U < UB:
        UB = U
        print("UB", UB)
        opty_harmonogram = Harmonogram
        print("U", U)
    [a, b, c] = blok.blok(Harmonogram, U)
    if c == -1:
        print("U w c == -1", U)
        return 0
    else:
        # print("Harmonogram:")
        # for i in Harmonogram:
        #     print(i)
        print("a ", a," b ", b," c ", c)

        r = min(Harmonogram[c+1:b+1]).r
        q = min(Harmonogram[c+1:b+1]).q
        print("r", r)
        print("q", q)
        p = 0
        for i in range(c+1, b+1):
            p = p + Harmonogram[i].p
        print("p", p)
        Harmonogram_c_r = copy.copy(Harmonogram[c].r)
        Harmonogram[c].r = max(Harmonogram[c].r, r + p)

        LB = schrageDistribution.SchrageWithDistributuion(NSetD)
        if LB < UB:
            Calier(NSetD2, UB)
        Harmonogram[c].r = Harmonogram_c_r

        Harmonogram_c_q = copy.copy(Harmonogram[c].q)
        Harmonogram[c].q = max(Harmonogram[c].q, q + p)

        LB = schrageDistribution.SchrageWithDistributuion(NSet)
        if LB < UB:
            Calier(NSet1, UB)
        Harmonogram[c].q = Harmonogram_c_q


Calier(Nset, 1299)





