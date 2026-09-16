name=input("Enter your name: ")
cls=int(input("Enter your class: "))
m1=int(input("Enter marks of subject 1: "))
m2=int(input("Enter marks of subject 2: "))
m3=int(input("Enter marks of subject 3: "))
m4=int(input("Enter marks of subject 4: "))
m5=int(input("Enter marks of subject 5: "))
total=m1+m2+m3+m4+m5
avg=total/5
print("Total marks of",name,"in class",cls,"is:",total)
if avg>=90:
    print("Grade: A")
elif avg>=80:
    print("Grade: B")
elif avg>=70:
    print("Grade: C")
elif avg>=60:
    print("Grade: D")
else:
    print("Grade: F")