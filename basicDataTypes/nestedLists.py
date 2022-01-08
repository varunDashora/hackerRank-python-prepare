nested_list = []
output=[]
finalOp=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    nested_list.append([name,score])
for i in nested_list:
    output.append(i[1])
secondLowestScore=sorted(set(output))[1]
for i in sorted(nested_list):
    if(i[1]==secondLowestScore):
        print(i[0])
