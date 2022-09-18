# Вам нужно реализовать функцию greet(), которая должна принимать несколько имён (как минимум одно!)
# и возвращать строку приветствия (см. примеры ниже).
#
# greet('Bob')
# # 'Hello, Bob!'
# greet('Moe', 'Mary')
# # 'Hello, Moe and Mary!'
# greet(*'ABC')
# # 'Hello, A and B and C!'


def greet(name, *args):
    result = 'Hello, ' + name
    for a in args:
        result += ' and ' + a
    return result + '!'
