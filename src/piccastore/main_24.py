from object.PizzaStore import PizzaStore


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


def main(ps):
    while True:
        print('Hello. 0 - Exit, 1 - all pizzas(), 2 - order, 3 - pizza_price_range')
        c = input('Your choise: ')
        match c:
            case '0':
                break
            case '1':
                ps.print_pizzas(ps.pizzas)
            case '2':
                ps.print_amount_check(ps.amount_check)
            case '3':
                pizza_price_range()
            case _:
                print('Wrong choise! Try again')

    print('Bay')


if __name__ == '__main__':
    ps = PizzaStore(pizzas)
    main = ps


