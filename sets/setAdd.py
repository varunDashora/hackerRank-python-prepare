# Enter your code here. Read input from STDIN. Print output to STDOUT
no_of_stamps=int(input())
countries=set()
for i in range(no_of_stamps):
    countries.add(input())
print(len(countries))
