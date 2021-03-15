#56. Merge Intervals - Leetcode
#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

#Example 1:
#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

#Example 2:
#Input: intervals = [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge_interval(input):
    
    input.sort()
    print(input)
    res = []
    res.append(input[0])
        
    for i in range(1, len(input)):
        
        a,b = input[i]
        
        if (res[-1][1] >= a and res[-1][1] <= b) or (b <= res[-1][1] and b >= res[-1][0]):
            
            res[-1] = [min(res[-1][0], a),max(res[-1][1],b)] 
            
        else:
            res.append([a,b])
            
    
    return res


input = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
final = merge_interval(input)

print(final)

    

    
