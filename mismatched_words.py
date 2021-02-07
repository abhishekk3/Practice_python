#Complete a function that returns a list containing all the mismatched words (case sensitive) between two given input strings # For example: # - string 1 : "Firstly this is the first string" # - string 2 : "Next is the second string" # # - output : ['Firstly', 'this', 'first', 'Next', 'second']

#1st method
def mismatch_word (s1,s2):
    
    str1 = s1.split(" ")
    str2 = s2.split(" ")
        
    lst = []
    
    for i in str1:
        if i.lower() not in s2.lower():
            lst.append(i)
            
    for i in str2:
        if i.lower() not in s1.lower():
            lst.append(i)
            
    print(lst)
    

#2nd method
def mismatch_word_set (s1,s2):
    
    str1 = set(s1.split(" "))
    str2 = set(s2.split(" "))
        
    lst = []
    
    lst.append(list(str1.symmetric_difference(str2)))
            
    print(lst)
    


s1="Firstly this is the first string"
s2="Next is the second string"
mismatch_word(s1,s2)
mismatch_word_set(s1,s2)

# output : ['Firstly', 'this', 'first', 'Next', 'second']
