# Enter your code here. Read input from STDIN. Print output to STDOUT
    
size_setA, listA = int(input()), map(int, input().split())
size_setB, listB = int(input()), map(int, input().split())
setA = set(listA)
setB = set(listB) 
symmetric_diff = sorted(setA.union(setB) - setA.intersection(setB))

for i in map(int, symmetric_diff):
    print(i)
