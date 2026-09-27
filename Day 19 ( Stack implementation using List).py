stack=[]
def push():
    element=input("Enter the element:")
    stack.append(element)
    print(element,"is pushed to stack")
def pop():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Removed element:",e)
def display():
    print("Stack elements are:",stack)
while True:
    print("Select operation 1.Push 2.Pop 3.Display 4.Quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Invalid Choice")