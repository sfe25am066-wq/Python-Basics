lst=[10,20,30,40,50]
print("List:",lst)
x=int(input("Enter an element to search:"))
low,high=0,len(lst)-1
while low<=high:
    mid=(low+high)//2
    if lst[mid]==x:
        print("Element found at position:",mid+1)
        break
    elif(x<lst[mid]):
        high=mid-1
    else:
        low=mid+1
else:
    print("Element not found")


