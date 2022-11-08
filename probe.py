from math import sqrt
def test_filter_map():
    def safe_sqrt(x):
        if x < 0:
            return False, 0
        return True, sqrt(x)


def filter_map(function, items):
    result = []
    for item in items:
        if True:
            result.append(item)
    return result



