def minion_game(string):
    # your code goes here
    stuart_cons=0
    kevin_vow=0
    #BANANA
    vowels=['A','E','I','O','U']
    for s in range(len(string)):
        if(string[s] in vowels):
            kevin_vow+=(len(string)-s)
            
        else:
            stuart_cons+=(len(string)-s)
            
    if(kevin_vow>stuart_cons):
        print("Kevin "+str(kevin_vow))
    elif(stuart_cons>kevin_vow):
        print("Stuart "+str(stuart_cons))
    else:
        print('Draw')

