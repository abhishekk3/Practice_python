
#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

#sum67([1, 2, 2]) → 5
#sum67([1, 2, 2, 6, 99, 99, 7]) → 5
#sum67([1, 1, 6, 7, 2]) → 4

#1st method
def sum67(a):

    sum = 0     
    i = 0        
    while i < len(a):
        if a[i] != 6:
            sum = sum + a[i]
            i += 1
        else:
            ind = a[i:].index(7)
            ind = ind + i
            if ind < len(a)-1:
                i = ind + 1
            else:
                break

    
    print(sum)
                
    
#2nd method
def sum67_new(nums):

    total_sum = 0
    skip_flag = False

    for number in nums:
        if number == 6:
            skip_flag = True # prepare to skip
            continue # skip this iteration
        if number == 7 and skip_flag == True:
            skip_flag = False # prepare to sum
            continue # skip this iteration
        if skip_flag == False:
            total_sum += number

    print(total_sum)

    
    
sum67_new([1, 2, 2])
sum67_new([1, 2, 2, 6, 99, 99, 7])
sum67_new([1, 1, 6, 7, 2])
sum67_new([2, 7, 6, 2, 6, 7, 2, 7])
