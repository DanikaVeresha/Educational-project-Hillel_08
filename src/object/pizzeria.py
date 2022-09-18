from object.pizza import Pizza
from object.check import Check

class Pizzeria(Pizza):
    def __init__(self, up_to_150_UAH, more_than_150_UAH, equal_to_150_UAH, func):
        super().__init__(self, idx, name, price, description)
        self.up_to_150_UAH = up_to_150_UAH
        self.more_than_150_UAH = more_than_150_UAH
        self.equal_to_150_UAH = equal_to_150_UAH
        self.func = func

    def decs(self, func):
        def inner():
            print('-------------Category of pizzas by pricing policy: -------------')
            func()
            print('----------------------------------------------------------------')

        return inner

    @decs
    def list_pizzas(self):
        pizzas_1 = filter(lambda item: self.price < 150, pizzas)
        for item in pizzas_1:
            print(f'the price of pizza is less than 150 UAH: {self.up_to_150_UAH}')
        pizzas_2 = filter(lambda item: self.price < 150, pizzas)
        for item in pizzas_2:
            print(f'the price of pizza is more than 150 UAH: {self.more_than_150_UAH}')
        pizzas_3 = filter(lambda item: self.price < 150, pizzas)
        for item in pizzas_3:
            print(f'the price of pizza is 150 UAH: {self.equal_to_150_UAH}')


pizzas = [
    Pizza(1, 'Hawaiian', 100, 'Chicken + pineapple + bakery + mozzarella + sauce'),
    Pizza(2, 'Carbonara', 110, 'Bacon + tavern + bakery + marinated + olives + mozzarella'),
    Pizza(3, 'M`yasna', 120, 'Bacon + salami + tomato + mozzarella'),
    Pizza(4, 'Margarita', 130, 'Tomato + mozzarella + sauce + salami'),
    Pizza(5, 'Mislivska', 140, 'Hunting sausages + salami + salted cucumber + garlic'),
    Pizza(6, 'Vegetable teriyaki', 150, 'Tomato + mushrooms + bell pepper + pickles'),
    Pizza(7, 'Pepperoni', 160, 'Pepperoni + italian herbs + mozzarella + signature sauce'),
    Pizza(8, 'Francesca', 170, 'Bacon + salami + mushrooms + tomato + olives + mozzarella'),
    Pizza(9, 'Four cheeses', 180, 'Dor bleu cheese + gouda cheese + cream cheese + mozzarella'),
    Pizza(10, 'Sharp', 200, 'Salami + tomatoes + bell pepper + green beans + sauce')
]

my_pizzas = Pizza
my_pizzas.pizza_description()
my_pizza1 = Pizzeria
my_pizza1.list_pizzas()
my_pizza1.decs()
order = Check
order.my_order()

