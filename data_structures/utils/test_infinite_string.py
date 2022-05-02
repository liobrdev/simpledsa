from pytest import fixture, mark, raises
from secrets import choice, randbelow
from string import ascii_letters, digits, punctuation, whitespace
from typing import Any

from .infinite_string import InfiniteString

chars = ascii_letters + digits + punctuation + whitespace


@fixture
def infinite_string() -> InfiniteString:
    return InfiniteString()


def test_infinite_string_success(infinite_string: InfiniteString):
    INF_STR = infinite_string
    random_string = ''.join(choice(chars) for i in range(randbelow(80) + 1))

    assert isinstance(INF_STR, str)
    assert random_string != INF_STR
    assert INF_STR > random_string
    assert INF_STR >= random_string
    assert random_string < INF_STR
    assert random_string <= INF_STR
    assert INF_STR == INF_STR
    assert INF_STR >= INF_STR
    assert INF_STR <= INF_STR

    assert -INF_STR == ''
    assert -INF_STR != random_string
    assert random_string > -INF_STR
    assert random_string >= -INF_STR
    assert -INF_STR < random_string
    assert -INF_STR <= random_string
    assert -INF_STR < INF_STR
    assert -INF_STR <= INF_STR
    assert INF_STR > -INF_STR
    assert INF_STR >= -INF_STR


@mark.parametrize('arg', [9, float('inf'), True, ['a'], ('a',), {'a': 0}])
def test_infinite_string_fail_eq(arg: Any, infinite_string: InfiniteString):
    with raises(TypeError) as e:
        infinite_string == arg

    assert (
        'Unsupported operand type(s) for ==:' +
        f" 'InfiniteString' and '{type(arg)}'"
    ) in str(e.value)


@mark.parametrize('arg', [9, float('inf'), True, ['a'], ('a',), {'a': 0}])
def test_infinite_string_fail_ge(arg: Any, infinite_string: InfiniteString):
    with raises(TypeError) as e:
        infinite_string >= arg

    assert (
        'Unsupported operand type(s) for >=:' +
        f" 'InfiniteString' and '{type(arg)}'"
    ) in str(e.value)


@mark.parametrize('arg', [9, float('inf'), True, ['a'], ('a',), {'a': 0}])
def test_infinite_string_fail_gt(arg: Any, infinite_string: InfiniteString):
    with raises(TypeError) as e:
        infinite_string > arg

    assert (
        'Unsupported operand type(s) for >:' +
        f" 'InfiniteString' and '{type(arg)}'"
    ) in str(e.value)


@mark.parametrize('arg', [9, float('inf'), True, ['a'], ('a',), {'a': 0}])
def test_infinite_string_fail_le(arg: Any, infinite_string: InfiniteString):
    with raises(TypeError) as e:
        infinite_string <= arg

    assert (
        'Unsupported operand type(s) for <=:' +
        f" 'InfiniteString' and '{type(arg)}'"
    ) in str(e.value)


@mark.parametrize('arg', [9, float('inf'), True, ['a'], ('a',), {'a': 0}])
def test_infinite_string_fail_lt(arg: Any, infinite_string: InfiniteString):
    with raises(TypeError) as e:
        infinite_string < arg

    assert (
        'Unsupported operand type(s) for <:' +
        f" 'InfiniteString' and '{type(arg)}'"
    ) in str(e.value)
