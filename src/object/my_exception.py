
class MyException(Exception):
    def __init__(self, price):
        self.price = price

    def filter_price(self):
        try:
            if self.price <= 0:
                raise MyException('Error, pizza price must be greater than 0 and be a natural number')
            print(f'{self.price} > 0')

        except Exception as x:
            print(x)
        else:
            print('Everything is fine')
        finally:
            print('You entered the wrong price value')


