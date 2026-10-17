lst=[3,5,8,4,2]
print("List:",lst)
for i in range(len(lst)):
    for j in range(len(lst)-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            print("Sorted list:",lst)

