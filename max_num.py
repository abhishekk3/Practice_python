
#Find a maximum of an interger which can be formed by inserting a digit(here 5) at any position in the given number.

def max_num(N):
    
    a='5'
    n=list(str(N))
    A=[]
      
    if len(n) == 1:
        print('5' + str(N),end='')
    else:
            for i in range(0,len(n)+1):
                n.insert(i,a)
                str1 = ''.join(str(i) for i in n)
                A.append(str1)
                n.pop(i)
            print(max(A))
max_num(528)
