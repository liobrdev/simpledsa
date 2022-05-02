from pytest import fixture, mark, raises
from typing import Any

from .prime_numbers import is_prime, next_prime


@fixture
def primes() -> list[int]:
    return [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
        149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
        227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
        307, 311, 313, 317,]


@fixture
def composites() -> list[int]:
    return [
        1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28,
        30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52,
        54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76,
        77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98,
        99, 100, 102,]


def test_is_prime_true(primes: list[int]):
    for n in primes:
        assert is_prime(n)


def test_is_prime_false(composites: list[int]):
    for n in composites:
        assert not is_prime(n)


def test_next_prime(primes: list[int]):
    index = 0

    while index < len(primes) - 1:
        assert next_prime(primes[index]) == primes[index + 1]
        index += 1

    assert next_prime(-100) == 2
    assert next_prime(-31) == 2
    assert next_prime(-2) == 2
    assert next_prime(-1) == 2
    assert next_prime(0) == 2
    assert next_prime(1) == 2


@mark.parametrize('arg', [9.9, True, ['a'], ('a',), {'a': 0}])
def test_is_prime_fail(arg: Any):
    with raises(TypeError) as e:
        is_prime(arg)

    assert 'Value must be an integer!' in str(e.value)


@mark.parametrize('arg', [9.9, True, ['a'], ('a',), {'a': 0}])
def test_next_prime_fail(arg: Any):
    with raises(TypeError) as e:
        next_prime(arg)

    assert 'Value must be an integer!' in str(e.value)
