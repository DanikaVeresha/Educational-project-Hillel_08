from homework.currency_pairs_list import *


class Course:
    def __init__(self, course, rate, available):
        self.course = course
        self.rate = rate
        self.available = available

    def __str__(self):
        for item in courseUAH:
            return f'\n Course: {item.course} | Rate: {item.rate}\n' \
                   f'\n Available: {item.available} USD\n'
        for item in courseUSD:
            return f'\n Course: {item.course} | Rate: {item.rate}\n' \
                   f'\n Available: {item.available} USD\n'
        for item in courseBCH:
            return f'\n Course: {item.course} | Rate: {item.rate}\n' \
                   f'\n Available: {item.available} USD\n'

