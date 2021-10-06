# pytest raises

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiplay(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ZeroDivisionError('can not division by zero.')
    return x / y