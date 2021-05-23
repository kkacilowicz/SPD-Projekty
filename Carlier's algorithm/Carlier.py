# Name: Carlier algorithm
# Authors: Kacper Kaciłowicz 248951, Weronika Jakubowska 248931
# Date: 23.05.2021


import Schrage as schrage
import SchrageWithDistribution as schrageDistribution
import blok as blok
import readFile

Nset=[]
filename = "SCHRAGE1.DAT"
[Nset, n] = readFile.readFile(filename)
# for i in Nset:
#     print(i)
# print(n)
Nset2 = []
Nset2 = Nset
print("Nset", Nset)
print("Nset2", Nset2)
Harmonogram = []
[Harmonogram, Cmax] = schrage.Schrage(Nset)
for i in Harmonogram:
    print(i)
print(Cmax)
print("Nset", Nset)
print("Nset2", Nset2)
LB = schrageDistribution.SchrageWithDistributuion(Nset2)
print("LB" + str(LB))







