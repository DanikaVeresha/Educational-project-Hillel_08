
x = [1, 2, 3, 1, 3]


def numbers():
    return [item for item in x if x.count(item) > 1]


print(numbers())


pawns = ({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
pawns1 = ({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})


def safe_pawns(pawns: set) -> int:
    num = 0
    for item in pawns:
        left_pawns = chr(ord(list(item)[0])-1) + chr(ord(list(item)[1])-1)
        right_pawns = chr(ord(list(item)[0])+1) + chr(ord(list(item)[1])-1)
        if left_pawns in pawns or right_pawns in pawns:
            num += 1
    return num


print(safe_pawns(pawns))


def safe_pawns_1(pawns1: set) -> int:
    num = 0
    for item in pawns1:
        left_pawns1 = chr(ord(list(item)[0])-1) + chr(ord(list(item)[1])-1)
        right_pawns1 = chr(ord(list(item)[0])+1) + chr(ord(list(item)[1])-1)
        if left_pawns1 in pawns1 or right_pawns1 in pawns1:
            num += 1
    return num


print(safe_pawns_1(pawns1))

