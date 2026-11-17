print("Postfix Expression Evaluation")
def evaluate_postfix(expression):
    stack=[]
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            b=stack.pop()
            a=stack.pop()
            if char=="+":
                stack.append(a+b)
            elif char=="-":
                stack.append(a-b)
            elif char=="*":
                stack.append(a*b)
            elif char=="/":
                stack.append(a/b)
    return stack.pop()
exp=input("Enter A Postfix Expression:")
result=evaluate_postfix(exp)
print("Result:",result)