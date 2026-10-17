print("Selection Sort")
lst=[5,3,8,4,2]
print("List:",lst)
for i in range(len(lst)):
    min_pos=i
    for j in range(i+1,len(lst)):
        if lst[j]<lst[min_pos]:
            min_pos=j
            lst[i],lst[min_pos]=lst[min_pos],lst[i]
print("Sorted List",lst)