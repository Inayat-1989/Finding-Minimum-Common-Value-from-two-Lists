list1 = list(map(int,input("Enter a list of values:").split()))
list2 = list(map(int,input("Enter a list of values:").split()))
list1, list2 = set(sorted(list1)), set(sorted(list2))
i,j = 0,0
for k in range(len(list1) + len(list2)):
    if list1[i] == list2[j]:
        print(list1[i])
    elif list1[i] < list2[j]:
        i = i + 1
    elif list1[i] > list2[j]:
        j = j + 1
    if i == len(list1) or j == len(list2):
        print(-1)
print(-1)
