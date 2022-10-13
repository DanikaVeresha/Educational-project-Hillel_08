

class Course:
    def __init__(self, course, rate, available):
        self.course = course
        self.rate = rate
        self.available = available

    def __str__(self):
        return f'Course: {self.course} | Rate: {self.rate}\n' \
               f'Available: {self.available} UAH\n'


