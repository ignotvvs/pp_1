import stack
import re

exp = input("Expression: ")

for i in exp:
    if re.search(r"\d",i):
        stack.push(int(i))
    else:
        if i == "+":
            a = stack.pop()
            b = stack.pop()
            stack.push(a+b)
        elif i == "-":
            a = stack.pop()
            b = stack.pop()
            stack.push(b-a)
        elif i == "*":
            a = stack.pop()
            b = stack.pop()
            stack.push(a*b)
        elif i == "/":
            a = stack.pop()
            b = stack.pop()
            stack.push(b/a)
        elif i == "=":
            print(stack.pop())
