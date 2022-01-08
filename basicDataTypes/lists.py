# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Example
# N = 4
# append 1
# append 2
# insert 3 1
# print

# append 1: Append 1 to the list, .
# append 2: Append 2 to the list, .
# insert 3 1 : Insert 3 at 1 index , .
# print : Print the array.
# Output:
# [1, 3, 2]

list_final = []
if __name__ == '__main__':
    N = int(raw_input())
    
    for i in range(N):
        operation = raw_input()
        splitted_opr=operation.split(" ")
        if(operation.startswith("insert")):
            list_final.insert(int(splitted_opr[1]), int(splitted_opr[2]))
        elif(operation.startswith("remove")):
            list_final.remove(int(splitted_opr[1]))
        elif(operation.startswith("append")):
            list_final.append(int(splitted_opr[1]))
        elif(operation.startswith("sort")):
            list_final.sort()
        elif(operation.startswith("pop")):
            list_final.pop()
        elif(operation.startswith("sort")):
            list_final.sort()
        elif(operation.startswith("reverse")):
            list_final.reverse()
        elif(operation.startswith("print")):
            print(list_final)
