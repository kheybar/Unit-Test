# Assert

# shoe = {'name': 'Nike', 'price': 300}

# def aplly_discount(product, discount):
    # price = product['price'] - discount
    # assert 0 <= price <= product['price'], 'Not Valid'
    # assert (0 <= price <= product['price'], 'Not Valid') => tuple = True!

    # return price

# print(aplly_discount(shoe, 20))

# اگر بخوایم ازرت رو غیر فعال کنیم کافی موقع اجرا از این دستور استفاده کنیم
# pytho -O file_name.py

# ------------- E2

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
