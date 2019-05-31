_author_ = 'Dmitry'


def perc(x,y):
    """
    What percentage of x is y
    :param x :
    :param y :
    :return:
    """
    one_proc = x/100
    result = y/one_proc
    return result


def print_perc(x,y):
    print(str(y) + ' is ' + str(perc(x,y)) + '%' + ' percent of ' + str(x))


print_perc(200, 50)


def sqrt(x):
    """
    Корень квадратный числа x
    :param x:
    :return sqrt:
    """
    sqr = x**0.5
    return sqr


print(sqrt(9))