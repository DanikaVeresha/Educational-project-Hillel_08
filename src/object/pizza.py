
class Pizza:
    def __init__(self, idx, name, price, description):
        self.idx = idx
        self.name = name
        self.price = price
        self.description = description

    def pizza_description(self):
        print(f'{self.idx}, {self.name}\n'
              f' description: {self.description}\n'
              f' price: {self.price} UAH')


my_pizza = Pizza
my_pizza.pizza_description()

#верно ли этот файл я сделала?


