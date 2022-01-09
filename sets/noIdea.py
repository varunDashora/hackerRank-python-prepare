# Enter your code here. Read input from STDIN. Print output to STDOUT

size_of_array,size_of_set =input().split()

array = input().split()
set_a = set(input().split())
set_b = set(input().split())
happiness=0
for i in array:
    if(i in set_a):       
        happiness+=1
    if(i in set_b):        
        happiness-=1
print(happiness)
