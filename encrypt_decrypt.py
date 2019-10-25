#Below function is to encrypt/decrypt the strings which are in the repititive sequence of characters

from collections import OrderedDict

def encrypt():

  s='abbhhiiii'
  A=[]
  sub=list(s)

  for letter in OrderedDict.fromkeys(s):
    count=0
    while letter in sub:
      count+=1
      sub.remove(letter)
    A.append((letter+str(count)))
    
  print(''.join(A))
  
def decrypt():
  s='a1b2c3d4'

  lst=list(s)
  A=[]

  for i in range(0,len(lst),2):
    a=str(lst[i])
    b=int(lst[i+1])
    c=a*b
    A.append(c)    

  print (''.join(A))

decrypt()
