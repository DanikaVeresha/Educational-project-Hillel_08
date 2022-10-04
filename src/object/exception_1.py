from object.my_exception import MyException


try:
    price = int(input('price: '))
    if price <= 0:
        raise MyException(price)
except Exception as x:
    print('Error,price value:', x, 'not correct')
else:
    print('Everything is fine')
finally:
    print('Verification done')




