import random


class Pizza:
    def __init__(self, idx, name, price, description):
        '''атрибуты 1 пицци'''
        self.idx = idx
        self.name = name
        self.price = price
        self.description = description

    def enter(self):
        '''выводит пицци на екран'''
        for item in Pizzas:
            print(f'{item.idx}. Pizza: {item.name} | -  {item.price} UAH\n'
                  f'Description: {item.description}\n')

    def check(self):
        '''вывод всех заказов за текущую дату'''
        order = random.randint(1, 6)
        print(f'Number of checks for the current day: {order}\n'
              f'Pizza: price_UAH - amount')
        check_order = random.sample(Pizzas, order)
        d = random.randint(1, 31)
        m = random.randint(1, 12)
        n = random.randint(1, 100)
        sum = 0
        for item in check_order:
            amount = random.randint(1, 3)
            sum1 = item.price * amount
            sum += sum1
            print(f'----------------------------------------------------------------\n'
                  f'{item.name}: {item.price} UAH - {amount}\n'
                  f'All by check: {sum1} UAH')
        print(f'----------------------------------------------------------------\n'
              f'Total for the check for the current day: {sum} UAH\n'
              f'data:_{d}/{m}/2022_, check_№:_{n}_\n'
              f'You were served by: - cashier:Veresha_Dasha\n'
              f'----------------------------------------------------------------')

    def pizza_price_range(self):
        '''фильтация пицц по цене'''
        pizzas_1 = filter(lambda item: item.price < 150, Pizzas)
        print(f'The price of pizza is less than 150 UAH:\n')
        for item in pizzas_1:
            print(f'{item.idx}. {item.name} - {item.price} UAH')
        pizzas_2 = filter(lambda item: item.price > 150, Pizzas)
        print(f'\nThe price of pizza is more than 150 UAH:\n')
        for item in pizzas_2:
            print(f'{item.idx}. {item.name} - {item.price} UAH')
        pizzas_3 = filter(lambda item: item.price == 150, Pizzas)
        print(f'\nThe price of pizza is 150 UAH:\n')
        for item in pizzas_3:
            print(f'{item.idx}. {item.name}\n')


Pizzas = Pizza(1, 'Hawaiian', 100, 'Chicken + pineapple + bakery + mozzarella + sauce'),\
         Pizza(2, 'Carbonara', 110, 'Bacon + tavern + bakery + marinated + olives + mozzarella'),\
         Pizza(3, 'M`yasna', 120, 'Bacon + salami + tomato + mozzarella'),\
         Pizza(4, 'Margarita', 130, 'Tomato + mozzarella + sauce + salami'),\
         Pizza(5, 'Mislivska', 140, 'Hunting sausages + salami + salted cucumber + garlic'),\
         Pizza(6, 'Vegetable teriyaki', 150, 'Tomato + mushrooms + bell pepper + pickles'),\
         Pizza(7, 'Pepperoni', 160, 'Pepperoni + italian herbs + mozzarella + signature sauce'),\
         Pizza(8, 'Francesca', 170, 'Bacon + salami + mushrooms + tomato + olives + mozzarella'),\
         Pizza(9, 'Four cheeses', 180, 'Dor bleu cheese + gouda cheese + cream cheese + mozzarella'),\
         Pizza(10, 'Sharp', 200, 'Salami + tomatoes + bell pepper + green beans + sauce')
