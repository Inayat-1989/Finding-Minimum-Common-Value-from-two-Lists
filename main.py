list1 = list(map(int,input("Enter a list of values:").split()))
list2 = list(map(int,input("Enter a list of values:").split()))
list1, list2 = set(sorted(list1)), set(sorted(list2))
intersection = list1 & list2
if intersection:
    print(min(intersection))
else:
    print(-1)
