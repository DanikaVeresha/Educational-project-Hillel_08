

class Price:
    """атрибуты по цене"""
    def __init__(self, up_to_150_UAH, above_150_UAH, equal_to_150_UAH):
        self.up = up_to_150_UAH
        self.above = above_150_UAH
        self.equal = equal_to_150_UAH


    @decs
    def pizza_price_range():
        pizzas_1 = filter(lambda item: item.price < 150, pizzas)
        for item in pizzas_1:
            print(f'the price of pizza is less than 150 UAH: {item.name}')
        pizzas_2 = filter(lambda item: item.price > 150, pizzas)
        for item in pizzas_2:
            print(f'the price of pizza is more than 150 UAH: {item.name}')
        pizzas_3 = filter(lambda item: item.price == 150, pizzas)
        for item in pizzas_3:
            print(f'the price of pizza is 150 UAH: {item.name}')

    #def __str__(self):
        #pizzas_1 = filter(lambda item: item.price < 150, pizzas)
        #for item in pizzas_1:
         #   return f'the price of pizza is less than 150 UAH: {self.name}' \
        #pizzas_2 = filter(lambda item: item.price > 150, pizzas)
        #for item in pizzas_2:
         #   return f'the price of pizza is more than 150 UAH: {self.name}
        #pizzas_3 = filter(lambda item: item.price == 150, pizzas)
        #for item in pizzas_3:
         #   return f'the price of pizza is 150 UAH: {self.name}'



Price = Price

print(Price)