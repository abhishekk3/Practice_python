#Problem Statement: Given an array of integers, we would like to determine whether the array is monotonic (non-decreasing/non-increasing) or not.
    
#Examples:
#1 2 5 5 8->true
#9 4 4 2 2->true
#1 4 6 3->false
#1 1 1 1 1 1->true

def monotonic_arr(arr):

    num = arr[1]
              
    if arr [0] < arr [1]:
        for i in range(2,len(arr)):
            if arr[i] < num:
                return False
        return True
                
                      
    elif arr [0] > arr [1]:
        for i in range(2,len(arr)):
            if arr[i] > num:
                return False
        return True
    
    else:
        return True
        
            
                
            
        
a= [10,10,10,9,14]
res=monotonic_arr(a)
print(res)
