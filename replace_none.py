#Replace None with next element from List. For eg.
#[None] ==> [None]
#[None,1,2] ==> [1,1,2]
#[1,None,2] ==> [1,2,2]
#[1,4,None,None,3]===> [1,4,3,3,3]


def replace_none(arr):
    
    for i in range(len(arr)):
        if arr[i] == None:
            for j in range(i+1,len(arr)):
                if arr[j] is not None and i+1 < len(arr):
                    arr.insert(i,arr[j])
                    arr.pop(j)
                    break
    
    print(arr)
    

a=[4,5,None,1,2,None,3]
replace_none(a)
