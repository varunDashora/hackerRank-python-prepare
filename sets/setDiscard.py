n = int(input())
s = set(map(int, input().split()))
operations = int(input())
for i in range(operations):
    command=input()
    if("pop" in command):
        s.pop()
    elif("discard" in command):
        s.discard(int(command.split()[1]))
    elif("remove" in command):
        s.remove(int(command.split()[1]))
print(sum(s))
