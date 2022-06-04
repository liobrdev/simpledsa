from pytest import mark, raises

from .binary_search_tree import BinarySearchTree as BST, Node


@mark.parametrize('args', [
    [(1, 'first'), (2, 'second'), (3, 'third')],
    [(1.0, 'first'), (2.0, 'second'), (3.0, 'third')],
    [('1', 'first'), ('2', 'second'), ('3', 'third')],
])
def test_initialize_bst_success(args):
    BST(*args)


@mark.parametrize('args', [
    [([1], 'first'), ([2], 'second'), ([3], 'third')],
    [((1.0,), 'first'), ((2.0,), 'second'), ((3.0,), 'third')],
    [({'1': 1}, 'first'), ({'2': 2}, 'second'), ({'3': 3}, 'third')],
])
def test_initialize_bst_fail_invalid_keys(args):
    with raises(TypeError) as e:
        BST(*args)

    assert (
        "Keys must be of type 'bytes', 'float', 'int', or 'str'!"
    ) in str(e.value)


@mark.parametrize('args', [
    [(1, 'first'), (2, 'second'), (3.0, 'third')],
    [(1.0, 'first'), ('2.0', 'second'), (3.0, 'third')],
    [(1, 'first'), ('2', 'second'), ('3', 'third')],
])
def test_initialize_bst_fail_same_key_types(args):
    with raises(TypeError) as e:
        BST(*args)

    assert 'All keys must have the same type!' in str(e.value)


@mark.parametrize('args', [
    [(1, 'first'), (2, 'second'), (3, 3.0)],
    [(1.0, 'first'), (2.0, 2), (3.0, 'third')],
    [('1', ['first']), ('2', 'second'), ('3', 'third')],
])
def test_initialize_bst_fail_same_value_types(args):
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
def test_initialize_bst_fail_non_tuple_types(args):
    with raises(TypeError) as e:
        BST(*args)

    assert 'All arguments must be key-value tuples!' in str(e.value)


def test_construct_bst_default_fail():
    with raises(ValueError) as e:
        BST((11, '11'), (6, '6'), (13, '13'), (5, '5'), (12, '12'), (13, '13'))

    assert (
        'Cannot construct valid binary search tree ' +
        'from provided sequence - remove duplicate keys!'
    ) in str(e.value)


def test_bst_traverse_level_order(
    example_perfect_bst_small: BST[str],
    example_perfect_bst_medium: BST[str],
    example_perfect_bst_large: BST[str],
):
    assert example_perfect_bst_small.traverse_level_order() == \
        [(2, 'second'), (1, 'first'), (3, 'third')]
    assert example_perfect_bst_medium.traverse_level_order() == [
        (4, 'fourth'), (2, 'second'), (6, 'sixth'), (1, 'first'), (3, 'third'),
        (5, 'fifth'), (7, 'seventh'),]
    assert example_perfect_bst_large.traverse_level_order() == [
        (8, 'eighth'), (4, 'fourth'), (12, 'twelfth'), (2, 'second'),
        (6, 'sixth'), (10, 'tenth'), (14, 'fourteenth'), (1, 'first'),
        (3, 'third'), (5, 'fifth'), (7, 'seventh'), (9, 'ninth'),
        (11, 'eleventh'), (13, 'thirteenth'), (15, 'fifteenth'),]


def test_bst_traverse_pre_order(
    example_perfect_bst_small: BST[str],
    example_perfect_bst_medium: BST[str],
    example_perfect_bst_large: BST[str],
):
    assert example_perfect_bst_small.traverse_pre_order() == \
        [(2, 'second'), (1, 'first'), (3, 'third')]
    assert example_perfect_bst_medium.traverse_pre_order() == [
        (4, 'fourth'), (2, 'second'), (1, 'first'), (3, 'third'), (6, 'sixth'),
        (5, 'fifth'), (7, 'seventh'),]
    assert example_perfect_bst_large.traverse_pre_order() == [
        (8, 'eighth'), (4, 'fourth'), (2, 'second'), (1, 'first'),
        (3, 'third'), (6, 'sixth'), (5, 'fifth'), (7, 'seventh'),
        (12, 'twelfth'), (10, 'tenth'), (9, 'ninth'), (11, 'eleventh'),
        (14, 'fourteenth'), (13, 'thirteenth'), (15, 'fifteenth'),]


def test_bst_traverse_in_order(
    example_perfect_bst_small: BST[str],
    example_perfect_bst_medium: BST[str],
    example_perfect_bst_large: BST[str],
):
    assert example_perfect_bst_small.traverse_in_order() == \
        [(1, 'first'), (2, 'second'), (3, 'third')]
    assert example_perfect_bst_medium.traverse_in_order() == [
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'),]
    assert example_perfect_bst_large.traverse_in_order() == [
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'), (8, 'eighth'), (9, 'ninth'),
        (10, 'tenth'), (11, 'eleventh'), (12, 'twelfth'), (13, 'thirteenth'),
        (14, 'fourteenth'), (15, 'fifteenth'),]


def test_binary_tree_traverse_post_order(
    example_perfect_bst_small: BST[str],
    example_perfect_bst_medium: BST[str],
    example_perfect_bst_large: BST[str],
):
    assert example_perfect_bst_small.traverse_post_order() == \
        [(1, 'first'), (3, 'third'), (2, 'second')]
    assert example_perfect_bst_medium.traverse_post_order() == [
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'),]
    assert example_perfect_bst_large.traverse_post_order() == [
        (1, 'first'), (3, 'third'), (2, 'second'), (5, 'fifth'),
        (7, 'seventh'), (6, 'sixth'), (4, 'fourth'), (9, 'ninth'),
        (11, 'eleventh'), (10, 'tenth'), (13, 'thirteenth'), (15, 'fifteenth'),
        (14, 'fourteenth'), (12, 'twelfth'), (8, 'eighth'),]


def test_bst_len(
    example_perfect_bst_small: BST[str],
    example_perfect_bst_medium: BST[str],
    example_perfect_bst_large: BST[str],
):
    assert len(example_perfect_bst_small) == 3
    assert len(example_perfect_bst_medium) == 7
    assert len(example_perfect_bst_large) == 15


def test_bst_height(
    example_perfect_bst_small: BST[str],
    example_perfect_bst_medium: BST[str],
    example_perfect_bst_large: BST[str],
):
    assert BST().height() == -1
    assert example_perfect_bst_small.height() == 1
    assert example_perfect_bst_medium.height() == 2
    assert example_perfect_bst_large.height() == 3

    t = BST((1, 'first'))
    assert t.height() == 0
    t._BinarySearchTree__root.left = Node(2, 'second') # type: ignore
    assert t.height() == 1
    t._BinarySearchTree__root.left.left = Node(4, 'fourth') # type: ignore
    assert t.height() == 2
    t._BinarySearchTree__root.left.right = Node(5, 'fifth') # type: ignore
    assert t.height() == 2
    t._BinarySearchTree__root.left.left = None # type: ignore
    t._BinarySearchTree__root.left.right = None # type: ignore
    assert t.height() == 1
    t._BinarySearchTree__root.left = None # type: ignore
    assert t.height() == 0
    t._BinarySearchTree__root = None # type: ignore
    assert t.height() == -1


def test_bst_copy(
    example_perfect_bst_small: BST[str],
    example_perfect_bst_medium: BST[str],
    example_perfect_bst_large: BST[str],
):
    empty: BST = BST()
    empty_copy = empty.copy()
    assert empty is not empty_copy
    assert empty.height() == -1
    assert empty_copy.height() == -1

    for tree in (
        example_perfect_bst_small,
        example_perfect_bst_medium,
        example_perfect_bst_large,
    ):
        copy = tree.copy()
        assert copy is not tree
        assert copy._BinarySearchTree__root is not None # type: ignore
        assert tree._BinarySearchTree__root is not None # type: ignore
        assert copy._BinarySearchTree__root is not ( # type: ignore
            tree._BinarySearchTree__root # type: ignore
        )
        assert copy._BinarySearchTree__root.data.key == ( # type: ignore
            tree._BinarySearchTree__root.data.key # type: ignore
        )
        assert copy._BinarySearchTree__root.data.value == ( # type: ignore
            tree._BinarySearchTree__root.data.value # type: ignore
        )
        assert copy.traverse_level_order() == tree.traverse_level_order()
        assert copy.traverse_pre_order() == tree.traverse_pre_order()
        assert copy.traverse_in_order() == tree.traverse_in_order()
        assert copy.traverse_post_order() == tree.traverse_post_order()
        assert copy.height() == tree.height()


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
    assert t._BinarySearchTree__root is None
    assert t._BinarySearchTree__key_type is None
    assert t._BinarySearchTree__value_type is None

    with raises(RuntimeError) as e:
        t.get('1')
    assert 'Key type not defined!' in str(e.value)

    t.put('1', 'first')
    assert t.get('1') == 'first'
    assert t._BinarySearchTree__root is not None
    assert t._BinarySearchTree__root.data.key == '1'
    assert t._BinarySearchTree__root.data.value == 'first'
    assert str(t._BinarySearchTree__key_type) == "<class 'str'>"
    assert str(t._BinarySearchTree__value_type) == "<class 'str'>"
    t['2'] = 'second'
    assert t.get('2') == 'second'
    assert t._BinarySearchTree__root.right.data.key == '2'
    assert t._BinarySearchTree__root.right.data.value == 'second'


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


def test_bst_remove_success(example_perfect_bst_large: BST[str]):
    t = example_perfect_bst_large

    assert t.get(2) == 'second'
    assert t._BinarySearchTree__root.left.left.data.key == 2 # type: ignore
    t.remove(2)
    with raises(KeyError) as e:
        t.get(2)
    assert 'Key 2 not found!' in str(e.value)
    assert t.traverse_in_order() == [
        (1, 'first'), (3, 'third'), (4, 'fourth'), (5, 'fifth'), (6, 'sixth'),
        (7, 'seventh'), (8, 'eighth'), (9, 'ninth'), (10, 'tenth'),
        (11, 'eleventh'), (12, 'twelfth'), (13, 'thirteenth'),
        (14, 'fourteenth'), (15, 'fifteenth'),]
    assert t._BinarySearchTree__root.left.left.data.key == 3 # type: ignore

    assert t.get(3) == 'third'
    t.remove(3)
    with raises(KeyError) as e:
        t.get(3)
    assert 'Key 3 not found!' in str(e.value)
    assert t.traverse_in_order() == [
        (1, 'first'), (4, 'fourth'), (5, 'fifth'), (6, 'sixth'),
        (7, 'seventh'), (8, 'eighth'), (9, 'ninth'), (10, 'tenth'),
        (11, 'eleventh'), (12, 'twelfth'), (13, 'thirteenth'),
        (14, 'fourteenth'), (15, 'fifteenth'),]
    assert t._BinarySearchTree__root.left.left.data.key == 1 # type: ignore

    assert t.get(1) == 'first'
    t.remove(1)
    with raises(KeyError) as e:
        t.get(1)
    assert 'Key 1 not found!' in str(e.value)
    assert t.traverse_in_order() == [
        (4, 'fourth'), (5, 'fifth'), (6, 'sixth'), (7, 'seventh'),
        (8, 'eighth'), (9, 'ninth'), (10, 'tenth'), (11, 'eleventh'),
        (12, 'twelfth'), (13, 'thirteenth'), (14, 'fourteenth'),
        (15, 'fifteenth'),]
    assert t._BinarySearchTree__root.left.data.key == 4 # type: ignore
    assert t._BinarySearchTree__root.left.left is None # type: ignore

    assert t.get(4) == 'fourth'
    del t[4]
    with raises(KeyError) as e:
        t.get(4)
    assert 'Key 4 not found!' in str(e.value)
    assert t.traverse_in_order() == [
        (5, 'fifth'), (6, 'sixth'), (7, 'seventh'), (8, 'eighth'),
        (9, 'ninth'), (10, 'tenth'), (11, 'eleventh'), (12, 'twelfth'),
        (13, 'thirteenth'), (14, 'fourteenth'), (15, 'fifteenth'),]
    assert t._BinarySearchTree__root.left.data.key == 6 # type: ignore
    assert t._BinarySearchTree__root.left.left.data.key == 5 # type: ignore

    assert t.get(8) == 'eighth'
    assert t._BinarySearchTree__root.data.key == 8 # type: ignore
    assert \
        t._BinarySearchTree__root.right.left.left.data.key == 9 # type: ignore
    del t[8]
    with raises(KeyError) as e:
        t.get(8)
    assert 'Key 8 not found!' in str(e.value)
    assert t.traverse_in_order() == [
        (5, 'fifth'), (6, 'sixth'), (7, 'seventh'), (9, 'ninth'),
        (10, 'tenth'), (11, 'eleventh'), (12, 'twelfth'), (13, 'thirteenth'),
        (14, 'fourteenth'), (15, 'fifteenth'),]
    assert t._BinarySearchTree__root.data.key == 9 # type: ignore
    assert t._BinarySearchTree__root.left.data.key == 6 # type: ignore
    assert t._BinarySearchTree__root.right.left.data.key == 10 # type: ignore
    assert \
        t._BinarySearchTree__root.right.left.right.data.key == ( # type: ignore
            11
        )
    assert t._BinarySearchTree__root.right.left.left is None # type: ignore

    assert t.get(12) == 'twelfth'
    assert t._BinarySearchTree__root.right.data.key == 12 # type: ignore
    assert \
        t._BinarySearchTree__root.right.right.left.data.key == ( # type: ignore
            13
        )
    del t[12]
    with raises(KeyError) as e:
        t.get(12)
    assert 'Key 12 not found!' in str(e.value)
    assert t.traverse_in_order() == [
        (5, 'fifth'), (6, 'sixth'), (7, 'seventh'), (9, 'ninth'),
        (10, 'tenth'), (11, 'eleventh'), (13, 'thirteenth'),
        (14, 'fourteenth'), (15, 'fifteenth'),]
    assert t._BinarySearchTree__root.data.key == 9 # type: ignore
    assert t._BinarySearchTree__root.right.data.key == 13 # type: ignore
    assert t._BinarySearchTree__root.right.right.data.key == 14 # type: ignore
    assert t._BinarySearchTree__root.right.right.left is None # type: ignore


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

