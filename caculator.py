def add(x,y):
    return print(x+y)

def subtract(x,y):
    return print(x-y)

def multiply(x,y):
    return print(x*y)

def divide(x,y):
    return print(x/y)

#######################################
a = int(input("Enter number: "))
b = int(input("Enter number: "))
op = input("Enter operator: ")

###################################
if op == "+":
    add(a,b)
    
elif op == "-":
    subtract(a,b)
    
elif op == "*":
    multiply(a,b)
    
elif op == "/":
    divide(a,b)
    
else:
    print("ERROR")