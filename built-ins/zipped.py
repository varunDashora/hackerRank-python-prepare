# Enter your code here. Read input from STDIN. Print output to STDOUT
students,subjects=map(int, input().split())
marks=[]
for _ in range(subjects):
    
    marks.append(list(map(float,input().split())))

for i in zip(*marks):
    print(sum(i)/len(i))
