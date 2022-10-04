from object.PIZZA import Pizza
import random
from object.OrderCheck import Check
from object.Checkline import CheckLine
from object.my_exception import MyException


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Pizzastore(metaclass=Singleton):
    '''атрибуты пиццерии'''
    def __init__(self, pizzas):
        self.price = None
        self.pizzas = ([Pizza(*item) for item in pizzas])
        self.checks = []
        self.pizzas_1 = filter(lambda item: item.price < 150, self.pizzas)
        self.pizzas_2 = filter(lambda item: item.price > 150, self.pizzas)
        self.pizzas_3 = filter(lambda item: item.price == 150, self.pizzas)

    def check(self, date, number, line):
        pass

    def add_random_check(self):
        '''добавляет каждую строку чека в общий чек'''
        check = Check(len(self.checks) + 1)
        amount_line = random.randint(1, 6)
        random_pizza_list = random.sample(self.pizzas, amount_line)
        sum = 0
        for item in random_pizza_list:
            amount = random.randint(1, 3)
            sum1 = item.price * amount
            sum += sum1
            checkline = CheckLine(amount, item)
            check.lines.append(checkline)
        check.calculate_total()
        self.checks.append(check)

    def calculate_checks(self):
        self.checks = sum([item.sum for item in self.checks])

    def filter_price(self):
        try:
            if self.price <= 0:
                raise MyException('Error')
        finally:
            print('You entered the wrong price value')

    def __str__(self):
        txt = f' \t Pizzas list: {self.pizzas}\n'
        txt += f' \t list pizzas for price then 150 UAH: {self.pizzas_1}\n'
        txt += f' \t list pizzas for price more 150 UAH: {self.pizzas_2}\n'
        txt += f' \t list pizzas price is 150 UAH: {self.pizzas_3}\n'
        for item in self.checks:
            txt += f'{item.pizza.name} \t {item.pizza.price} \t {item.amount_pizzas} \t {item.sum}\n' \
                   f'Total for check: {item.total}\n'
        txt += f'{self.checks}\n'
        return txt







