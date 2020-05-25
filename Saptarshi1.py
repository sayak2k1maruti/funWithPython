t = int(input())
outputList = []
for i in range(0,t):
    list = input().split()
    if len(list) == 3:
        outputList.insert(int(list[1]),int(list[2]))
    elif list[0] == "remove":
        outputList.remove(int(list[1]))
    elif list[0] == "append":
        outputList.append(int(list[1]))
    elif list[0] == "sort":
        outputList.sort()
    elif list[0] == "pop":
        outputList.pop()
    elif list[0] == "reverse":
        outputList.reverse()
    elif list[0] == "print":
        print(outputList)
