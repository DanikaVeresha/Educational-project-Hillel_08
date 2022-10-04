from object.my_exception import MyException


try:
    price = int(input('price: '))
    if price <= 0:
        raise MyException(price)
except MyException as x:
    print('Error,price value:', x, 'not correct')
except ValueError as z:
    print('The value', z, 'must be an integer and a natural number')
else:
    print('Everything is fine')
finally:
    print('Verification done')




