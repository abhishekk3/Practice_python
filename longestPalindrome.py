#Given a string s, return the longest palindromic substring in s.

#Example 1:
#Input: s = "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.
#
#Example 2:
#Input: s = "cbbd"
#Output: "bb"
#
#Example 3:
#Input: s = "a"
#Output: "a"
#
#Example 4:
#Input: s = "ac"
#Output: "a"

#1st method
def longestPalindrome(s: str):
    
        palin_list = []
    
        if len(s) == 1:
            return(s)
        
        if len(s) == 2:
            if s == s[::-1]:
                return (s)
            else:
                return(s[0])
             
    
        if len(s) > 2:
        
            for i in range(len(s)):
                st = ""
                st = st + s[i]
                for j in range(i+1,len(s)):
                    st = st + s[j]
                    if st == st[::-1]:
                        palin_list.append(st)
                s.replace(s[i],"",1)
                    
            if not palin_list:
                return (s[0])
            else:

                a = max((map(len,palin_list)))

                b = [i for i in palin_list if len(i) == a]

                return(b[0])

#2nd method

def longestPalindrome():
    
        s = "abcda"
        
        l = []
    
        if len(s) == 1:
            print(s)

        if len(s) >= 2:
            
            for i in range(len(s)):
                
                for j in range(len(s),i+1,-1):
                    
                    if s[i:j] == s[i:j][::-1]:
                        l.append(s[i:j])
                        break
            
            if not l:
                print (s[0])
            else:
        
                x = max(map(len,l))

                a = [ele for ele in l if len(ele) == x]

                print(a[0])

                    
