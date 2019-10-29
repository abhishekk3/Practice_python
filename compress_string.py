def compress(S):

    A=list(S)
    B=[]
    count=1
    
    for i in range(len(A)-1):
        if A[i] != A[i+1]:
            B.append(A[i])
            if count > 1:
                B.append(str(count))
                count=1
        else:
            count+=1
        if i == len(A) - 2 and count > 1:
            B.append(A[i]+str(count))
        if i == len(A) - 2 and count == 1:
            B.append(A[i+1])
                            
 
    print(''.join(B))
compress('brrrroocodeee')
