# The query language is a very simple regular expression-like language, with one special character: . (the dot character), which means EXACTLY ONE character (it can be any character). 
# So, for example, 'c.t' would match 'cat' as the dot matches any character. There may be any number of dot characters in the query (or none).
# If it matches, return 'Available' otherwise 'NA'
#There are some examples below, feel free to ask for clarification.

#Word List: [cat, bat, rat, drat, dart, drab]

#Queries:
#cat -> true
#c.t -> true
#.at -> true
#..t -> true
#d..t -> true
#dr.. -> true
#... -> true
#.... -> true
#
#..... -> false
#h.t -> false
#c. -> false

def spell_checker(list_dict, word):
    
    word_len = len(word)
    
    tmp_lst = []
    
    for i in list_dict:
        if len(i) == word_len:
            tmp_lst.append(i)
            
            
    if not tmp_lst:
        print('NA')
    elif word in tmp_lst:
        print('Available')
    else:
        found = True
        for i in range(word_len):
            
            if found:
            
                if word[i] == '.':
                    continue
                else:
                    s = word[i]

                    for x in range(len(tmp_lst)):
                        if s == tmp_lst[x][i]:
                            found = True
                            break
                        else:
                            found = False
            else:
                print('NA')
                break
