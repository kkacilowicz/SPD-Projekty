import Schrage as schrage
import blok as blok
import readFile

Nset=[]
filename = "SCHRAGE1.DAT"
[Nset, n] = readFile.readFile(filename)
for i in Nset:
    print(i)
print(n)

Harmonogram = []
[Harmonogram, Cmax] = schrage.Schrage(Nset)
for i in Harmonogram:
    print(i)
print(Cmax)





