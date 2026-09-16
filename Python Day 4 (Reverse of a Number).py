n=int(input("Enter a number: " ))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+n%10
    n//=10
print("The reverse of the number is:", rev) 