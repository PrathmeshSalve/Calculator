"""
LEVEL : B E G I N N E R.
-----------------------------------------------------------
Project - Calculator.
-----------------------------------------------------------
"""

from art import logo

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

calc = {"+":add,"-":sub,"*":mul,"/":div}

def call():
    print(logo)

    num1 = float(input("What is the first number?: "))
    for symbol in calc:
        print(symbol)
    check = 0
    
    while check == 0:
        operation = input("Pick an operation: ")
        op = calc[operation]
        num2 = float(input("What is the next number?: "))
        answer = op(num1,num2)

        print(f"{num1} {operation} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculator.") == "n":
            check += 1
            call()
        else:
            num1 = answer
call()