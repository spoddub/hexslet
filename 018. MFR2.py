# В этом упражнении вам предстоит попрактиковаться в использовании встроенных функций map(), filter(),
# reduce() (эту нужно импортировать из functools).
# На их основе вам нужно реализовать три функции: keep_truthful(), abs_sum() и walk().
#
# Функция keep_truthful() должна принимать на вход итерируемый источник значений и возвращать итератор,
# отдающий только те значения из источника, которые "истинны" (вам пригодится функция operator.truth).

def abs_sum(nums):
    return sum(abs(i) for i in nums)


print(abs_sum([-3, 7]))
print(abs_sum([]))
print(abs_sum([42]))


def keep_truthful(lst):
    return filter(lambda x: x, lst)


print(list(keep_truthful([True, False, "", "foo"])))


def walk(data, lst):
    for i in lst:
        data = data[i]
    return data


print(walk({'a': {7: {'b': 42}}}, ["a", 7, "b"]))
print(walk({'a': {7: {'b': 42}}}, ["a", 7]))
