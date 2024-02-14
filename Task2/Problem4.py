n = int(input())
list = []

for iteration in range(n):
    userinput= input().split()

    if userinput[0] == 'insert':
        list.insert(int(userinput[1]),int (userinput[2]))
    elif userinput[0] == 'print':
        print(list)
    elif userinput[0] == 'remove':
        list.remove(int(userinput[1]))
    elif userinput[0] == 'append':
        list.append(int(userinput[1]))
    elif userinput[0] == 'sort':
        list.sort()
    elif userinput[0] == 'pop':
        list.pop()
    elif userinput[0] == 'reverse':
        list.reverse()