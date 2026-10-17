lst=[10,25,30,45,50]
print(lst)
x=int(input("Enter an element to search:"))
found=False
for i in range(len(lst)):
    if lst[i]==x:
        print("Element found at position:",i+1)
        found=True
        break
if not found:
    print("Element not Found")
    