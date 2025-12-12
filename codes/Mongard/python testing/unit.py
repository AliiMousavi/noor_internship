def add(x, y):
    return x + y

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def devision(a , b):
    if b == 0:
        raise ZeroDivisionError("can't devide by zero")
    return a / b