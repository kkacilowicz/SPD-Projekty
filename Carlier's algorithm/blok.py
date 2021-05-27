
def PositionB(list, Cmax):
     B = -1
     for i in list:
          if(i.C+i.q == Cmax):
               B = list.index(i)
     return B


def PositionA(list, Cmax, B):
     Bq = list[B].q
     a = -1

     for i in reversed(range(0, len(list))):
          sum = 0
          for j in range(i, B+1):
               sum = sum + list[j].p
          if (list[i].r + sum + Bq) == Cmax:
               a = i
     return a

def PositionC(A, B, list):
     Bq = list[B].q
     C = -1
     for i in list[A:B]:
          if(i.q < Bq):
               C = list.index(i)
     return C

def blok (list, Cmax):
     B = PositionB(list, Cmax)
     A = PositionA(list, Cmax, B)
     if B == -1:
          A = -1
          C = -1
     elif A >= B:
          C = -1
     else:
          C = PositionC(A, B, list)
     return A, B, C



