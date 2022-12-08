import math

def power(x,y) -> float:
    """
    Takes the x parameter to the power of the y parameter
    :param x: base number
    :param y: exponent
    :return:  resulting number
    """
    if y < 0:
        return math.pow(x,y)
    if y == 1:
        return x
    else:
        return(x * power(x,y-1))

def cat_ears(n) -> int:
    """
    Count the ears of cats based on the amount given
    :param n: amount of cats
    :return: total cat ears
    """
    if n == 0:
        return 0
    else:
        return 2 + cat_ears(n-1)

def alien_ears(n) -> int:
    """
    Count the ears of aliens based on the amount given, odd aliens have 3 ears, even aliens have 2 ears
    :param n: amount of aliens
    :return: total alien ears
    """
    if n == 1:
        return 2
    elif n % 2 == 0:
        return 3 + alien_ears(n-1)
    else:
        return 2 + alien_ears(n-1)