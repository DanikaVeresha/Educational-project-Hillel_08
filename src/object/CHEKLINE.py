from object.pizza import Pizza


class CheckLine:
    '''атрибуты строки чека'''
    def __init__(self, amount_pizzas, pizza: Pizza):
        self.amount_pizzas = amount_pizzas
        self.pizza = pizza
        self.sum = self.amount_pizzas * self.pizza.price

    def __str__(self):
        '''вивод пицци и ее количества, сумма по строке(1 заказ)'''
        return f'{self.pizza.name}: {self.pizza.price} UAH - {self.amount_pizzas}\n' \
               f'сумма за количество пицц одного вида: {self.sum} UAH\n'

    def append(self, checkline):
        pass


