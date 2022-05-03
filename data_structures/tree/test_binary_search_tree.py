from pytest import mark, raises
from typing import Any

from . import BinarySearchTree as BST


@mark.parametrize('args', [
    [(1, 'first'), (2, 'second'), (3, 'third')],
    [(1.0, 'first'), (2.0, 'second'), (3.0, 'third')],
    [('1', 'first'), ('2', 'second'), ('3', 'third')],
])
def test_initialize_bst_success(args: list[tuple[int | float | str, str]]):
    BST(*args)


@mark.parametrize('args', [
    [([1], 'first'), ([2], 'second'), ([3], 'third')],
    [((1.0,), 'first'), ((2.0,), 'second'), ((3.0,), 'third')],
    [({'1': 1}, 'first'), ({'2': 2}, 'second'), ({'3': 3}, 'third')],
])
def test_initialize_bst_fail_invalid_keys(args: list[tuple[Any, str]]):
    with raises(TypeError) as e:
        BST(*args)

    assert "Keys must be of type 'int', 'float', or 'str'!" in str(e.value)


@mark.parametrize('args', [
    [(1, 'first'), (2, 'second'), (3.0, 'third')],
    [(1.0, 'first'), ('2.0', 'second'), (3.0, 'third')],
    [(1, 'first'), ('2', 'second'), ('3', 'third')],
])
def test_initialize_bst_fail_same_key_types(args: list[tuple[Any, str]]):
    with raises(TypeError) as e:
        BST(*args)

    assert 'All keys must have the same type!' in str(e.value)


@mark.parametrize('args', [
    [(1, 'first'), (2, 'second'), (3, 3.0)],
    [(1.0, 'first'), (2.0, 2), (3.0, 'third')],
    [('1', ['first']), ('2', 'second'), ('3', 'third')],
])
def test_initialize_bst_fail_same_value_types(
    args: list[tuple[int | float | str, Any]],
):
    with raises(TypeError) as e:
        BST(*args)

    assert 'All values must have the same type!' in str(e.value)


@mark.parametrize('args', [
    ['first', 'second', 'third'],
    [1, 2, 3],
    [1.0, 2.0, 3.0],
    [{'first': 11}, {'second': 22}, {'third': 33}],
    [[10, 11], [21, 22], [32, 33]],
])
def test_initialize_bst_fail_non_tuple_types(args: list[Any]):
    with raises(TypeError) as e:
        BST(*args)

    assert 'All arguments must be key-value tuples!' in str(e.value)


def test_construct_bst_default_success():
    small = BST((2, 'second'), (1, 'first'), (3, 'third'))
    assert small.traverse_level_order() == \
        [(2, 'second'), (1, 'first'), (3, 'third')]
    assert small.traverse_pre_order() == \
        [(2, 'second'), (1, 'first'), (3, 'third')]
    assert small.traverse_in_order() == \
        [(1, 'first'), (2, 'second'), (3, 'third')]
    assert small.traverse_post_order() == \
        [(1, 'first'), (3, 'third'), (2, 'second')]

    medium = BST(
        (4, 'fourth'), (2, 'second'), (6, 'sixth'), (1, 'first'), (3, 'third'),
        (5, 'fifth'), (7, 'seventh'),)
    assert medium.traverse_level_order() == [
        (4, 'fourth'), (2, 'second'), (6, 'sixth'), (1, 'first'), (3, 'third'),
        (5, 'fifth'), (7, 'seventh'),]
    assert medium.traverse_pre_order() == [
        (4, 'fourth'), (2, 'second'), (1, 'first'), (3, 'third'), (6, 'sixth'),
        (5, 'fifth'), (7, 'seventh'),]
    assert medium.traverse_in_order() == [
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'),]
    assert medium.traverse_post_order() == [
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'),]

    large = BST(
        (8, 'eighth'), (4, 'fourth'), (12, 'twelfth'), (2, 'second'),
        (6, 'sixth'), (10, 'tenth'), (14, 'fourteenth'), (1, 'first'),
        (3, 'third'), (5, 'fifth'), (7, 'seventh'), (9, 'ninth'),
        (11, 'eleventh'), (13, 'thirteenth'), (15, 'fifteenth'),)
    assert large.traverse_level_order() == [
        (8, 'eighth'), (4, 'fourth'), (12, 'twelfth'), (2, 'second'),
        (6, 'sixth'), (10, 'tenth'), (14, 'fourteenth'), (1, 'first'),
        (3, 'third'), (5, 'fifth'), (7, 'seventh'), (9, 'ninth'),
        (11, 'eleventh'), (13, 'thirteenth'), (15, 'fifteenth'),]
    assert large.traverse_pre_order() == [
        (8, 'eighth'), (4, 'fourth'), (2, 'second'), (1, 'first'),
        (3, 'third'), (6, 'sixth'), (5, 'fifth'), (7, 'seventh'),
        (12, 'twelfth'), (10, 'tenth'), (9, 'ninth'), (11, 'eleventh'),
        (14, 'fourteenth'), (13, 'thirteenth'), (15, 'fifteenth'),]
    assert large.traverse_in_order() == [
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'), (8, 'eighth'), (9, 'ninth'),
        (10, 'tenth'), (11, 'eleventh'), (12, 'twelfth'), (13, 'thirteenth'),
        (14, 'fourteenth'), (15, 'fifteenth'),]
    assert large.traverse_post_order() == [
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'), (9, 'ninth'),
        (11, 'eleventh'), (10, 'tenth'), (13, 'thirteenth'), (15, 'fifteenth'),
        (14, 'fourteenth'), (12, 'twelfth'), (8, 'eighth'),]


def test_construct_bst_default_fail():
    with raises(ValueError) as e:
        BST((11, '11'), (6, '6'), (13, '13'), (5, '5'), (12, '12'), (13, '13'))

    assert (
        'Cannot construct valid binary search tree ' +
        'from provided sequence - remove duplicate values!'
    ) in str(e.value)


def test_construct_bst_level_order_success():
    small = BST((2, 'second'), (1, 'first'), (3, 'third'), level_order=True)
    assert small.traverse_level_order() == \
        [(2, 'second'), (1, 'first'), (3, 'third')]
    assert small.traverse_pre_order() == \
        [(2, 'second'), (1, 'first'), (3, 'third')]
    assert small.traverse_in_order() == \
        [(1, 'first'), (2, 'second'), (3, 'third')]
    assert small.traverse_post_order() == \
        [(1, 'first'), (3, 'third'), (2, 'second')]

    medium = BST(
        (4, 'fourth'), (2, 'second'), (6, 'sixth'), (1, 'first'), (3, 'third'),
        (5, 'fifth'), (7, 'seventh'), level_order=True,)
    assert medium.traverse_level_order() == [
        (4, 'fourth'), (2, 'second'), (6, 'sixth'), (1, 'first'), (3, 'third'),
        (5, 'fifth'), (7, 'seventh'),]
    assert medium.traverse_pre_order() == [
        (4, 'fourth'), (2, 'second'), (1, 'first'), (3, 'third'), (6, 'sixth'),
        (5, 'fifth'), (7, 'seventh'),]
    assert medium.traverse_in_order() == [
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'),]
    assert medium.traverse_post_order() == [
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'),]

    large = BST(
        (8, 'eighth'), (4, 'fourth'), (12, 'twelfth'), (2, 'second'),
        (6, 'sixth'), (10, 'tenth'), (14, 'fourteenth'), (1, 'first'),
        (3, 'third'), (5, 'fifth'), (7, 'seventh'), (9, 'ninth'),
        (11, 'eleventh'), (13, 'thirteenth'), (15, 'fifteenth'),
        level_order=True,)
    assert large.traverse_level_order() == [
        (8, 'eighth'), (4, 'fourth'), (12, 'twelfth'), (2, 'second'),
        (6, 'sixth'), (10, 'tenth'), (14, 'fourteenth'), (1, 'first'),
        (3, 'third'), (5, 'fifth'), (7, 'seventh'), (9, 'ninth'),
        (11, 'eleventh'), (13, 'thirteenth'), (15, 'fifteenth'),]
    assert large.traverse_pre_order() == [
        (8, 'eighth'), (4, 'fourth'), (2, 'second'), (1, 'first'),
        (3, 'third'), (6, 'sixth'), (5, 'fifth'), (7, 'seventh'),
        (12, 'twelfth'), (10, 'tenth'), (9, 'ninth'), (11, 'eleventh'),
        (14, 'fourteenth'), (13, 'thirteenth'), (15, 'fifteenth'),]
    assert large.traverse_in_order() == [
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'), (8, 'eighth'), (9, 'ninth'),
        (10, 'tenth'), (11, 'eleventh'), (12, 'twelfth'), (13, 'thirteenth'),
        (14, 'fourteenth'), (15, 'fifteenth'),]
    assert large.traverse_post_order() == [
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'), (9, 'ninth'),
        (11, 'eleventh'), (10, 'tenth'), (13, 'thirteenth'), (15, 'fifteenth'),
        (14, 'fourteenth'), (12, 'twelfth'), (8, 'eighth'),]


def test_construct_bst_level_order_fail():
    with raises(ValueError) as e:
        BST(
            (11, '11'), (6, '6'), (13, '13'), (5, '5'), (12, '12'), (10, '10'),
            level_order=True,)

    assert (
        'Cannot construct valid binary search tree ' +
        'from provided level-order sequence!'
    ) in str(e.value)


def test_construct_bst_pre_order_success():
    small = BST((2, 'second'), (1, 'first'), (3, 'third'), pre_order=True)
    assert small.traverse_level_order() == \
        [(2, 'second'), (1, 'first'), (3, 'third')]
    assert small.traverse_pre_order() == \
        [(2, 'second'), (1, 'first'), (3, 'third')]
    assert small.traverse_in_order() == \
        [(1, 'first'), (2, 'second'), (3, 'third')]
    assert small.traverse_post_order() == \
        [(1, 'first'), (3, 'third'), (2, 'second')]

    medium = BST(
        (4, 'fourth'), (2, 'second'), (1, 'first'), (3, 'third'), (6, 'sixth'),
        (5, 'fifth'), (7, 'seventh'), pre_order=True,)
    assert medium.traverse_level_order() == [
        (4, 'fourth'), (2, 'second'), (6, 'sixth'), (1, 'first'), (3, 'third'),
        (5, 'fifth'), (7, 'seventh'),]
    assert medium.traverse_pre_order() == [
        (4, 'fourth'), (2, 'second'), (1, 'first'), (3, 'third'), (6, 'sixth'),
        (5, 'fifth'), (7, 'seventh'),]
    assert medium.traverse_in_order() == [
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'),]
    assert medium.traverse_post_order() == [
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'),]

    large = BST(
        (8, 'eighth'), (4, 'fourth'), (2, 'second'), (1, 'first'),
        (3, 'third'), (6, 'sixth'), (5, 'fifth'), (7, 'seventh'),
        (12, 'twelfth'), (10, 'tenth'), (9, 'ninth'), (11, 'eleventh'),
        (14, 'fourteenth'), (13, 'thirteenth'), (15, 'fifteenth'),
        pre_order=True,)
    assert large.traverse_level_order() == [
        (8, 'eighth'), (4, 'fourth'), (12, 'twelfth'), (2, 'second'),
        (6, 'sixth'), (10, 'tenth'), (14, 'fourteenth'), (1, 'first'),
        (3, 'third'), (5, 'fifth'), (7, 'seventh'), (9, 'ninth'),
        (11, 'eleventh'), (13, 'thirteenth'), (15, 'fifteenth'),]
    assert large.traverse_pre_order() == [
        (8, 'eighth'), (4, 'fourth'), (2, 'second'), (1, 'first'),
        (3, 'third'), (6, 'sixth'), (5, 'fifth'), (7, 'seventh'),
        (12, 'twelfth'), (10, 'tenth'), (9, 'ninth'), (11, 'eleventh'),
        (14, 'fourteenth'), (13, 'thirteenth'), (15, 'fifteenth'),]
    assert large.traverse_in_order() == [
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'), (8, 'eighth'), (9, 'ninth'),
        (10, 'tenth'), (11, 'eleventh'), (12, 'twelfth'), (13, 'thirteenth'),
        (14, 'fourteenth'), (15, 'fifteenth'),]
    assert large.traverse_post_order() == [
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'), (9, 'ninth'),
        (11, 'eleventh'), (10, 'tenth'), (13, 'thirteenth'), (15, 'fifteenth'),
        (14, 'fourteenth'), (12, 'twelfth'), (8, 'eighth'),]


def test_construct_bst_pre_order_fail():
    with raises(ValueError) as e:
        BST(
            (5, '5'), (3, '3'), (4, '4'), (1, '1'), (6, '6'), (10, '10'),
            pre_order=True,)

    assert (
        'Cannot construct valid binary search tree ' +
        'from provided pre-order sequence!'
    ) in str(e.value)


def test_construct_bst_in_order_success():
    small = BST((1, 'first'), (2, 'second'), (3, 'third'), in_order=True)
    assert small.traverse_level_order() == \
        [(2, 'second'), (1, 'first'), (3, 'third')]
    assert small.traverse_pre_order() == \
        [(2, 'second'), (1, 'first'), (3, 'third')]
    assert small.traverse_in_order() == \
        [(1, 'first'), (2, 'second'), (3, 'third')]
    assert small.traverse_post_order() == \
        [(1, 'first'), (3, 'third'), (2, 'second')]

    medium = BST(
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'), in_order=True,)
    assert medium.traverse_level_order() == [
        (4, 'fourth'), (2, 'second'), (6, 'sixth'), (1, 'first'), (3, 'third'),
        (5, 'fifth'), (7, 'seventh'),]
    assert medium.traverse_pre_order() == [
        (4, 'fourth'), (2, 'second'), (1, 'first'), (3, 'third'), (6, 'sixth'),
        (5, 'fifth'), (7, 'seventh'),]
    assert medium.traverse_in_order() == [
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'),]
    assert medium.traverse_post_order() == [
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'),]

    large = BST(
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'), (8, 'eighth'), (9, 'ninth'),
        (10, 'tenth'), (11, 'eleventh'), (12, 'twelfth'), (13, 'thirteenth'),
        (14, 'fourteenth'), (15, 'fifteenth'), in_order=True,)
    assert large.traverse_level_order() == [
        (8, 'eighth'), (4, 'fourth'), (12, 'twelfth'), (2, 'second'),
        (6, 'sixth'), (10, 'tenth'), (14, 'fourteenth'), (1, 'first'),
        (3, 'third'), (5, 'fifth'), (7, 'seventh'), (9, 'ninth'),
        (11, 'eleventh'), (13, 'thirteenth'), (15, 'fifteenth'),]
    assert large.traverse_pre_order() == [
        (8, 'eighth'), (4, 'fourth'), (2, 'second'), (1, 'first'),
        (3, 'third'), (6, 'sixth'), (5, 'fifth'), (7, 'seventh'),
        (12, 'twelfth'), (10, 'tenth'), (9, 'ninth'), (11, 'eleventh'),
        (14, 'fourteenth'), (13, 'thirteenth'), (15, 'fifteenth'),]
    assert large.traverse_in_order() == [
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'), (8, 'eighth'), (9, 'ninth'),
        (10, 'tenth'), (11, 'eleventh'), (12, 'twelfth'), (13, 'thirteenth'),
        (14, 'fourteenth'), (15, 'fifteenth'),]
    assert large.traverse_post_order() == [
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'), (9, 'ninth'),
        (11, 'eleventh'), (10, 'tenth'), (13, 'thirteenth'), (15, 'fifteenth'),
        (14, 'fourteenth'), (12, 'twelfth'), (8, 'eighth'),]


def test_construct_bst_in_order_fail():
    with raises(ValueError) as e:
        BST((1, '1'), (2, '2'), (4, '4'), (3, '3'), (5, '5'), in_order=True)

    assert (
        'Cannot construct valid binary search tree ' +
        'from provided in-order sequence!'
    ) in str(e.value)


def test_construct_bst_post_order_success():
    small = BST((1, 'first'), (3, 'third'), (2, 'second'), post_order=True)
    assert small.traverse_level_order() == \
        [(2, 'second'), (1, 'first'), (3, 'third')]
    assert small.traverse_pre_order() == \
        [(2, 'second'), (1, 'first'), (3, 'third')]
    assert small.traverse_in_order() == \
        [(1, 'first'), (2, 'second'), (3, 'third')]
    assert small.traverse_post_order() == \
        [(1, 'first'), (3, 'third'), (2, 'second')]

    medium = BST(
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'), post_order=True,)
    assert medium.traverse_level_order() == [
        (4, 'fourth'), (2, 'second'), (6, 'sixth'), (1, 'first'), (3, 'third'),
        (5, 'fifth'), (7, 'seventh'),]
    assert medium.traverse_pre_order() == [
        (4, 'fourth'), (2, 'second'), (1, 'first'), (3, 'third'), (6, 'sixth'),
        (5, 'fifth'), (7, 'seventh'),]
    assert medium.traverse_in_order() == [
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'),]
    assert medium.traverse_post_order() == [
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'),]

    large = BST(
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'), (9, 'ninth'),
        (11, 'eleventh'), (10, 'tenth'), (13, 'thirteenth'), (15, 'fifteenth'),
        (14, 'fourteenth'), (12, 'twelfth'), (8, 'eighth'), post_order=True,)
    assert large.traverse_level_order() == [
        (8, 'eighth'), (4, 'fourth'), (12, 'twelfth'), (2, 'second'),
        (6, 'sixth'), (10, 'tenth'), (14, 'fourteenth'), (1, 'first'),
        (3, 'third'), (5, 'fifth'), (7, 'seventh'), (9, 'ninth'),
        (11, 'eleventh'), (13, 'thirteenth'), (15, 'fifteenth'),]
    assert large.traverse_pre_order() == [
        (8, 'eighth'), (4, 'fourth'), (2, 'second'), (1, 'first'),
        (3, 'third'), (6, 'sixth'), (5, 'fifth'), (7, 'seventh'),
        (12, 'twelfth'), (10, 'tenth'), (9, 'ninth'), (11, 'eleventh'),
        (14, 'fourteenth'), (13, 'thirteenth'), (15, 'fifteenth'),]
    assert large.traverse_in_order() == [
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'), (8, 'eighth'), (9, 'ninth'),
        (10, 'tenth'), (11, 'eleventh'), (12, 'twelfth'), (13, 'thirteenth'),
        (14, 'fourteenth'), (15, 'fifteenth'),]
    assert large.traverse_post_order() == [
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'), (9, 'ninth'),
        (11, 'eleventh'), (10, 'tenth'), (13, 'thirteenth'), (15, 'fifteenth'),
        (14, 'fourteenth'), (12, 'twelfth'), (8, 'eighth'),]


def test_construct_bst_post_order_fail():
    with raises(ValueError) as e:
        BST(
            (1, '1'), (3, '3'), (4, '4'), (6, '6'), (7, '7'), (2, '2'),
            (5, '5'), post_order=True,)

    assert (
        'Cannot construct valid binary search tree ' +
        'from provided post-order sequence!'
    ) in str(e.value)


def test_bst_get_success(example_perfect_bst_small: BST[str]):
    assert example_perfect_bst_small.get(1) == 'first'
    assert example_perfect_bst_small.get(2) == 'second'
    assert example_perfect_bst_small.get(3) == 'third'
    assert example_perfect_bst_small[1] == 'first'
    assert example_perfect_bst_small[2] == 'second'
    assert example_perfect_bst_small[3] == 'third'


def test_bst_get_fail_runtimeerror():
    t = BST()

    with raises(RuntimeError) as e:
        t.get(1)

    assert 'Key type not defined!' in str(e.value)


def test_bst_get_fail_keyerror(example_perfect_bst_small: BST[str]):
    with raises(KeyError) as e:
        example_perfect_bst_small.get(4)

    assert 'Key 4 not found!' in str(e.value)


def test_bst_get_fail_typeerror(example_perfect_bst_small: BST[str]):
    with raises(TypeError) as e:
        example_perfect_bst_small.get('1')

    assert f"Key must be of type <class 'int'>!" in str(e.value)


def test_bst_put_success_insert(example_perfect_bst_small: BST[str]):
    with raises(KeyError) as e:
        example_perfect_bst_small.get(4)
    assert 'Key 4 not found!' in str(e.value)

    example_perfect_bst_small.put(4, 'fourth')
    assert example_perfect_bst_small.get(4) == 'fourth'
    example_perfect_bst_small[5] = 'fifth'
    assert example_perfect_bst_small.get(5) == 'fifth'


def test_bst_put_success_update(example_perfect_bst_small: BST[str]):
    assert example_perfect_bst_small.get(3) == 'third'
    example_perfect_bst_small.put(3, 'new_third')
    assert example_perfect_bst_small.get(3) == 'new_third'
    example_perfect_bst_small[3] = 'newer_third'
    assert example_perfect_bst_small.get(3) == 'newer_third'


def test_bst_put_success_empty():
    t = BST()
    assert t._root is None
    assert t._key_type is None
    assert t._value_type is None

    with raises(RuntimeError) as e:
        t.get('1')
    assert 'Key type not defined!' in str(e.value)

    t.put('1', 'first')
    assert t.get('1') == 'first'
    assert t._root is not None
    assert t._root.key == '1'
    assert t._root.value == 'first'
    assert str(t._key_type) == "<class 'str'>"
    assert str(t._value_type) == "<class 'str'>"
    t['2'] = 'second'
    assert t.get('2') == 'second'
    assert t._root.right.key == '2'
    assert t._root.right.value == 'second'


def test_bst_put_fail_invalid_key(example_perfect_bst_small: BST[str]):
    with raises(TypeError) as e:
        example_perfect_bst_small.put((4,), 'fourth') # type: ignore

    assert 'Invalid key!' in str(e.value)


def test_bst_put_fail_typeerror_key(example_perfect_bst_small: BST[str]):
    with raises(TypeError) as e:
        example_perfect_bst_small.put('4', 'fourth')

    assert f"Key must be of type <class 'int'>!" in str(e.value)


def test_bst_put_fail_typeerror_value(example_perfect_bst_small: BST[str]):
    with raises(TypeError) as e:
        example_perfect_bst_small.put(4, 400) # type: ignore

    assert f"Value must be of type <class 'str'>!" in str(e.value)


def test_bst_remove_success(example_perfect_bst_small: BST[str]):
    assert example_perfect_bst_small.get(3) == 'third'
    example_perfect_bst_small.remove(3)
    with raises(KeyError) as e:
        example_perfect_bst_small.get(3)
    assert 'Key 3 not found!' in str(e.value)

    assert example_perfect_bst_small.get(2) == 'second'
    del example_perfect_bst_small[2]
    with raises(KeyError) as e:
        example_perfect_bst_small.get(2)
    assert 'Key 2 not found!' in str(e.value)


def test_bst_remove_fail_invalid_key(example_perfect_bst_small: BST[str]):
    with raises(TypeError) as e:
        example_perfect_bst_small.remove((4,)) # type: ignore

    assert 'Invalid key!' in str(e.value)


def test_bst_remove_fail_typeerror_key(example_perfect_bst_small: BST[str]):
    with raises(TypeError) as e:
        example_perfect_bst_small.remove('4')

    assert f"Key must be of type <class 'int'>!" in str(e.value)


def test_bst_remove_fail_keyerror(example_perfect_bst_small: BST[str]):
    with raises(KeyError) as e:
        example_perfect_bst_small.remove(4)

    assert 'Key 4 not found!' in str(e.value)

