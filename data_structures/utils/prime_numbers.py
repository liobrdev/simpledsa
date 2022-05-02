from math import sqrt


def is_prime(n: int) -> bool:
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError('Value must be an integer!')

    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    else:
        return False


def next_prime(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError('Value must be an integer!')

    if n <= 1:
        return 2
    n += 1

    while True:
        if is_prime(n):
            return n
        n += 1
