#This is one of the leetcode problem where we have given a string and we need to 
#find the length of the longest substring without repeating characters.
#1st method
def long_substr(s):

  S=list(s)
  A=[]
  l=0
  B=[]

  for i in range(len(S)):
    if S[i] not in A:
      A.append(S[i])
      if len(B) < len(A):
        B=A.copy()
  
    else:
      if l <= len(A):
        l=len(A)
      A.clear()
      A.append(S[i])
      #print(A)

  print(l)
  print(''.join(B))
  
  
#2nd method
def lengthOfLongestSubstring(s: str):
    
    listt = list(s[0])
    st = s[0]
    ls = []
    i = 1
    
    while i < len(s):
        
        if s[i] != s[i-1] and s[i] not in listt:
            st += s[i]
            listt.append(s[i])
            i += 1
        else:
            ls.append(st)
            s = s.replace(s[0],'',1)
            st=""
            listt.clear()
            
            if len(s) > 0:
                listt = list(s[0])
                st = s[0]
                i = 1
            else:
                break
                
    ls.append(s)
    ls = set(ls)
    
    max_len = max(map(len,ls))
    print(max_len)
    
    a = [i for i in ls if len(i) == max_len]
    print(a)

long_substr('abcabcbb')
long_substr('bbbbbbbbbb')
long_substr('pwwkew')
