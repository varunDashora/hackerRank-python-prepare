def merge_the_tools(string, k):
    # your code goes here
    tempList=[]
    
    for i in range(0, len(string), k):
        sub_str_list = list(string[i:i+k])
        temp_ch = ""
        for char in sub_str_list:
            if(temp_ch == "" or (char not in temp_ch)):
                temp_ch+=char
            elif(char in temp_ch):
                pass
        print(temp_ch)                

