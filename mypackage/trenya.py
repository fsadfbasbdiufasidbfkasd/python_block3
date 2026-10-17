def num_square(n):
    square_list = []
    for i in n:
        i **= 2
        square_list.append(i)
    return square_list

numbers = [1, 2, 3, 4]
print(num_square(numbers))


def gen_number(n):
    for i in n:
        i = i ** 2
        yield i

numbers = [1, 2, 3, 4]
print(list(gen_number(numbers)))