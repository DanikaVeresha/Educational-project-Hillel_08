from object.Checkline import CheckLine
import random


class Check:
    '''атрибуты чека'''
    def __init__(self, month, date, number, line: CheckLine):
        self.lines = line
        self.number = number
        self.date = date
        self.month = month
        self.total = 0

    def dec_1(self):
        '''формирует данные чека'''
        self.date = random.randint(1, 31)
        self.month = random.randint(1, 12)
        self.number = random.randint(1, 100)

    def calculate_total(self):
        '''читает сумму всего чека'''
        self.lines = []
        self.total = sum([item.sum for item in self.lines])

    def __str__(self):
        txt = f' ----------------------------------------------------------------\n'
        txt += f' \t Пиццерия DASHKA \n\t чек_№: {self.number}_\n'
        txt += f' \t Дата:_{self.date}/{self.month}/2022_\n'
        txt += f' \t Итого по чеку: {self.total} UAH\n'
        txt += f' \t Вас обслуживал: - касир: Veresha_Dasha\n'
        txt += f' \t ------------------------------------------------------------\n'
        for item in [self.lines]:
            txt += f' \t {item.pizza.name} \t {item.pizza.price} \t {item.amount_pizzas} \t {item.sum}\n'
        txt += f' \t Всего по чеку: {self.total}\n'
        return txt

