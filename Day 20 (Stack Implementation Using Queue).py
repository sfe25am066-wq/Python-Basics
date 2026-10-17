queue=[]
def enqueue():
    element=input("Enter an element to Queue:")
    queue.append(element)
    print("Enqueued element:",element)
def dequeue():
    if not queue:
        print ("Queue is empty")
    else:
        print("Dequeued:",queue.pop(0))
def display():
    print("Queue:",queue)
while True:
    print ("\n 1.Enqueue 2.Dequeue 3.Display 4.Exit")
    choice=(int(input("Enter Your Choice:")))
    if(choice==1):
        enqueue()
    elif(choice==2):
        dequeue()
    elif(choice==3):
        display()
    elif(choice==4):
        break
    else:
        print("Invalid Choice")