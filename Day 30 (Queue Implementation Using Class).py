print("Queue Implementation Using Class")
class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if not self.queue:
            return "Queue is Empty"
        return self.queue.pop(0)
    def display(self):
        print("Queue:",self.queue)
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Dequeued:",q.dequeue())
q.display()