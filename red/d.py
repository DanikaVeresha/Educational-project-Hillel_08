import random


class CoffeDashka:
    '''атрибуты кофейни'''
    def __init__(self, tea, price, coffe, price1):
        self.coffe = coffe
        self.tea = tea
        self.price = price
        self.price1 = price1
        self.total = 0
        self.total1 = 0
        self.total2 = 0
        self.amount = 0
        self.amount1 = 0
        self.v = 0

    def meniu(self):
        '''выводить меню'''
        print(f'Напиток: {self.coffe}: цена: {self.price1} грн\n'
              f'Напиток: {self.tea}: цена: {self.price} грн')

    def order(self):
        '''готовить кофе'''
        self.amount = random.randint(1, 3)
        self.amount1 = random.randint(1, 6)
        self.total1 = self.amount * self.price
        self.total2 = self.amount1 * self.price1
        self.total = self.total2 + self.total1
        print(f'Ваш заказ:\n'
              f'{self.coffe}: цена: {self.price1}, количество: {self.amount1} - готов\n'
              f'чай {self.tea}: цена: {self.price}, количество: {self.amount} - готов\n'
              f'Всего к оплате: {self.total}')

    def list_meniu_for_price(self):
        '''выводить кофе по цене'''
        self.v = filter(lambda a: a.price1 <= 200, self.x)
        print(f'кофе по/до цене 200грн: {self.v}')


x = CoffeDashka('green', 100, 'latte', 200)
x1 = CoffeDashka('black', 120, 'Capuchino', 180)
x2 = CoffeDashka('red', 250, 'Americano', 300)

x.meniu()
x1.meniu()
x2.meniu()
x.order()
x1.order()
x2.order()
print(x.__dict__)
print(x1.__dict__)
print(x2.__dict__)