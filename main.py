list1 = list(map(int,input("Enter a list of values:").split()))
list2 = list(map(int,input("Enter a list of values:").split()))
list1, list2 = set(sorted(list1)), set(sorted(list2))
i,j = 0,0
while i < len(list1) and j < len(list2):
    if list1[i] == list2[j]:
        print(list1[i])
    elif list1[i] < list2[j]:
        i += 1
    else:
        j += 1
print(-1)
