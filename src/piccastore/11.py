
x = [1, 2, 3, 1, 3]


def numbers():
    return [item for item in x if x.count(item) > 1]


print(numbers())


