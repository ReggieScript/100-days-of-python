import os
#Mathematical Functions

def add(n1,n2):
    """ Adds two numbers"""
    return n1+n2

def sub(n1,n2):
    """Subtracts two numbers"""
    return n1-n2

def multiply(n1,n2):
    """Multiplies two numbers"""
    return n1*n2

def divide(n1,n2):
    """Divides two numbers"""
    return n1/n2

operations={
"+": add,
"-": sub,
"*": multiply,
"/": divide,
}

def calculator():
    num1=int(input("What's the first number?\n"))
    cont=True
    while cont:
        num2=int(input("What's the second number?\n"))
        for key in operations:
            print(key)
        op=input("Pick an operation from those shown above:\n")
        result=operations[op](num1,num2)
        print(f"{num1} {op} {num2} = {result}")
        if input(f"Would you like to keep using the calculator with {result}? Type 'y' or 'type'n' to exit.")== 'y':
            num1=result
        else:
            cont= False
            os.system('cls')
        
calculator()