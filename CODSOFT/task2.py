def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "invalid operation"
    return x/y
def modular(x,y):
    if y==0:
        return "invalid operation"
    else:
        return x%y
while True:
    print("Options:")
    print("Enter '+' or 'add' for addition")
    print("Enter '-' or 'sub' for subtraction")
    print("Enter '*' or 'mul' for multiplication")
    print("Enter '/' or 'div' for divison")
    print("Enter '%' or 'rem' for remainder")
    print("Enter 'q' or 'quit' to quit the program")
    operation=input()
    if operation == 'quit' or operation=='q':
        break
    if operation not in('add','sub','mul','div','rem','+','-','*','/','%'):
        print("invalid input")
        continue
    a=float(input("Enter first number"))
    b=float(input("Enter second number"))
    if operation=="add" or operation=="+":
        r=add(a,b)
    elif operation=="sub" or operation=="-":
        r=sub(a,b)
    elif operation=="mul" or operation=="*":
        r=multiply(a,b)
    elif operation=="div" or operation=="/":
        r=divide(a,b)
    elif operation=="rem" or operation=="%":
        r=modular(a,b)
    print(f"Result: {r}")
print("Program has ended")