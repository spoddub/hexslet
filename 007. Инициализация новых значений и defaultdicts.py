# Цель упражнения — функция collect_indexes().
# Эта функция должна принимать на вход коллекцию (некий iterator/iterable)
# и возвращать словарь (или подобная ему коллекция!),
# где ключом будет элемент коллекции, а значением для ключа — список индексов коллекции, п
# о которым встречается этот элемент.


def collect_indexes(col):
    res = {}
    for idx, el in enumerate(col):
        res.setdefault(el, []).append(idx)
    return res
