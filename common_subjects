#This functions is to find out the common subjects between the pair of students.

from itertools import combinations
def course(A):
  D={}
  for x,y in A:
    if x not in D.keys():
      D[x] = [y]
    else:
      D[x].append(y)
  #print(D)

  E={}

  for (k1, v1), (k2, v2) in combinations(D.items(),2):
    s=set(v1).intersection(v2)
    E[k1,k2]=list(s)

  for i,j in E.items():
    print(str(i) + '-->' + str(j))

A=[(1,'Math'), (1,'Science'), (2,'Science'),(1,'English'),(3,'Math'), (2,'English'),(2,'Geo'),(3,'Science'), (4,'GK'),(1,'GK') ]
course(A) 
