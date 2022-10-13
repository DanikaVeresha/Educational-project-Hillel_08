from homework.currency_pairs_list import *


class ReadingRemains:
    def __init__(self, original_balance, course, request):
        self.courseUAH = ([course(*item) for item in courseUAH])
        self.courseUSD = ([course(*item) for item in courseUSD])
        self.courseBCH = ([course(*item) for item in courseBCH])
        self.original_balance = original_balance
        self.request = request
        self.final_balance = self.original_balance - self.request

    def __str__(self):
        for item in courseUAH:
            return f'\nCourse: {item.course} |Available: {item.available} UAH\n' \
                   f'\nExchange request: {self.request} UAH\n' \
                   f'\nAvailable balance after the transaction: {self.final_balance} UAH\n'
        for item in courseUSD:
            return f'\nCourse: {item.course} |Available: {item.available} USD\n' \
                   f'\nExchange request: {self.request} USD\n' \
                   f'\nAvailable balance after the transaction: {self.final_balance} USD\n'
        for item in courseBCH:
            return f'\nCourse: {item.course} |Available: {item.available} BCH\n' \
                   f'\nExchange request: {self.request} BCH\n' \
                   f'\nAvailable balance after the transaction: {self.final_balance} BCH\n'



