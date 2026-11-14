print("Stack Implementation Using Class")
class stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.stack:
            return"stack is empty"
        return self.stack.pop()
    def display(self):
        print("Stack:",self.stack)
s=stack()
s.push(20)
s.push(30)
s.push(40)
s.display()
print("Popped:",s.pop())
s.display()