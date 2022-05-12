from pytest import mark, raises
from typing import Any

from . import BinaryTree
from ..utils import BinaryTreeNode as Node


@mark.parametrize('args', [
    [('first', 1), ('second', 2), ('third', 3)],
    [(1, 'first'), (2, 'second'), (3, 'third')],
    [('first', '1'), ('second', '2'), ('third', '3')],
    [('first', 1.0), ('second', 2.0), ('third', 3.0)],
    [(1.01, 'first'), (2.01, 'second'), (3.01, 'third')],
    [(1, 100), (2, None), (3, 300)],
    [(1.02, None), (2.02, 200), (3.02, 300)],
])
def test_initialize_binary_tree_success(args: list[tuple[Any, Any]]):
    BinaryTree(*args)


@mark.parametrize('args', [
    [('first', 1), (2, 2), ('third', 3)],
    [(1, 'first'), (2.02, 'second'), (3, 'third')],
    [('first', '1'), (2.0, '2'), ('third', '3')],
    [('first', 1.0), ('second', 2.0), (3, 3.0)],
    [(1.01, 'first'), (2.01, 'second'), (3, 'third')],
    [(1, 100), (2, 200), (None, 300)],
    [(1.02, 100), ('2.02', 200), (3.02, None)],
])
def test_initialize_binary_tree_fail_keys(args: list[tuple[Any, Any]]):
    with raises(TypeError) as e:
        BinaryTree(*args)

    assert 'All keys must have the same type!' in str(e.value)


@mark.parametrize('args', [
    [('first', 1), (None, 2), ('third', 3)],
    [(None, 'first'), (2, 'second'), (3, 'third')],
])
def test_initialize_binary_tree_fail_null_key(args: list[tuple[Any, Any]]):
    with raises(TypeError) as e:
        BinaryTree(*args)

    assert 'Keys must not be None!' in str(e.value)


@mark.parametrize('args', [
    [('first', 1), ('second', 2.0), ('third', 3)],
    [(1, 'first'), (2, 22), (3, 'third')],
    [('first', '1'), ('second', 2), ('third', '3')],
    [('first', 1.0), ('second', 2.0), ('third', [30])],
    [(1.01, 'first'), (2.01, ('second',)), (3.01, 'third')],
    [(1, 100), (2, None), (3, 3.00)],
    [(1.02, None), (2.02, '200'), (3.02, 300)],
])
def test_initialize_binary_tree_fail_values(args: list[tuple[Any, Any]]):
    with raises(TypeError) as e:
        BinaryTree(*args)

    assert 'All values must have the same type!' in str(e.value)


@mark.parametrize('args', [
    ['first', 'second', 3],
    [1, 2, 'third'],
    [False, 'True', False],
    [[1, 'first'], (2, 'second'), (3, 'third')],
    [{'first': 11}, ('second', 22), {'third': 33}],
    [[10, 11], [21, 22], (32, 33)],
])
def test_initialize_binary_tree_fail_non_tuple(args: list):
    with raises(TypeError) as e:
        BinaryTree(*args)

    assert 'All arguments must be key-value tuples!' in str(e.value)


def test_binary_tree_len(
    example_perfect_binary_tree_small: BinaryTree[str, int],
    example_perfect_binary_tree_medium: BinaryTree[str, int],
    example_perfect_binary_tree_large: BinaryTree[str, int],
):
    assert len(example_perfect_binary_tree_small) == 3
    assert len(example_perfect_binary_tree_medium) == 7
    assert len(example_perfect_binary_tree_large) == 15


def test_binary_tree_traverse_level_order(
    example_perfect_binary_tree_small: BinaryTree[str, int],
    example_perfect_binary_tree_medium: BinaryTree[str, int],
    example_perfect_binary_tree_large: BinaryTree[str, int],
):
    assert example_perfect_binary_tree_small.traverse_level_order() == \
        [('first', 1), ('second', 2), ('third', 3)]
    assert example_perfect_binary_tree_medium.traverse_level_order() == [
        ('first', 1), ('second', 2), ('third', 3), ('fourth', 4), ('fifth', 5),
        ('sixth', 6), ('seventh', 7),]
    assert example_perfect_binary_tree_large.traverse_level_order() == [
        ('first', 1), ('second', 2), ('third', 3), ('fourth', 4), ('fifth', 5),
        ('sixth', 6), ('seventh', 7), ('eighth', 8), ('ninth', 9),
        ('tenth', 10), ('eleventh', 11), ('twelfth', 12), ('thirteenth', 13),
        ('fourteenth', 14), ('fifteenth', 15),]


def test_binary_tree_traverse_pre_order(
    example_perfect_binary_tree_small: BinaryTree[str, int],
    example_perfect_binary_tree_medium: BinaryTree[str, int],
    example_perfect_binary_tree_large: BinaryTree[str, int],
):
    assert example_perfect_binary_tree_small.traverse_pre_order() == \
        [('first', 1), ('second', 2), ('third', 3)]
    assert example_perfect_binary_tree_medium.traverse_pre_order() == [
        ('first', 1), ('second', 2), ('fourth', 4), ('fifth', 5), ('third', 3),
        ('sixth', 6), ('seventh', 7),]
    assert example_perfect_binary_tree_large.traverse_pre_order() == [
        ('first', 1), ('second', 2), ('fourth', 4), ('eighth', 8),
        ('ninth', 9), ('fifth', 5), ('tenth', 10), ('eleventh', 11),
        ('third', 3), ('sixth', 6), ('twelfth', 12), ('thirteenth', 13),
        ('seventh', 7), ('fourteenth', 14), ('fifteenth', 15),]


def test_binary_tree_traverse_in_order(
    example_perfect_binary_tree_small: BinaryTree[str, int],
    example_perfect_binary_tree_medium: BinaryTree[str, int],
    example_perfect_binary_tree_large: BinaryTree[str, int],
):
    assert example_perfect_binary_tree_small.traverse_in_order() == \
        [('second', 2), ('first', 1), ('third', 3)]
    assert example_perfect_binary_tree_medium.traverse_in_order() == [
        ('fourth', 4), ('second', 2), ('fifth', 5), ('first', 1), ('sixth', 6),
        ('third', 3), ('seventh', 7),]
    assert example_perfect_binary_tree_large.traverse_in_order() == [
        ('eighth', 8), ('fourth', 4), ('ninth', 9), ('second', 2),
        ('tenth', 10), ('fifth', 5), ('eleventh', 11), ('first', 1),
        ('twelfth', 12), ('sixth', 6), ('thirteenth', 13), ('third', 3),
        ('fourteenth', 14), ('seventh', 7), ('fifteenth', 15),]


def test_binary_tree_traverse_post_order(
    example_perfect_binary_tree_small: BinaryTree[str, int],
    example_perfect_binary_tree_medium: BinaryTree[str, int],
    example_perfect_binary_tree_large: BinaryTree[str, int],
):
    assert example_perfect_binary_tree_small.traverse_post_order() == \
        [('second', 2), ('third', 3), ('first', 1)]
    assert example_perfect_binary_tree_medium.traverse_post_order() == [
        ('fourth', 4), ('fifth', 5), ('second', 2), ('sixth', 6),
        ('seventh', 7), ('third', 3), ('first', 1),]
    assert example_perfect_binary_tree_large.traverse_post_order() == [
        ('eighth', 8), ('ninth', 9), ('fourth', 4), ('tenth', 10),
        ('eleventh', 11), ('fifth', 5), ('second', 2), ('twelfth', 12),
        ('thirteenth', 13), ('sixth', 6), ('fourteenth', 14),
        ('fifteenth', 15), ('seventh', 7), ('third', 3), ('first', 1),]


def test_binary_tree_traverse_boundaries(
    example_perfect_binary_tree_small: BinaryTree[str, int],
    example_perfect_binary_tree_medium: BinaryTree[str, int],
    example_perfect_binary_tree_large: BinaryTree[str, int],
):
    assert example_perfect_binary_tree_small.traverse_boundaries() == \
        [('first', 1), ('second', 2), ('third', 3)]
    assert example_perfect_binary_tree_medium.traverse_boundaries() == [
        ('first', 1), ('second', 2), ('fourth', 4), ('fifth', 5), ('sixth', 6),
        ('seventh', 7), ('third', 3),]
    assert example_perfect_binary_tree_large.traverse_boundaries() == [
        ('first', 1), ('second', 2), ('fourth', 4), ('eighth', 8),
        ('ninth', 9), ('tenth', 10), ('eleventh', 11), ('twelfth', 12),
        ('thirteenth', 13), ('fourteenth', 14), ('fifteenth', 15),
        ('seventh', 7), ('third', 3),]


def test_binary_tree_height(
    example_perfect_binary_tree_small: BinaryTree[str, int],
    example_perfect_binary_tree_medium: BinaryTree[str, int],
    example_perfect_binary_tree_large: BinaryTree[str, int],
):
    assert BinaryTree().height() == -1
    assert example_perfect_binary_tree_small.height() == 1
    assert example_perfect_binary_tree_medium.height() == 2
    assert example_perfect_binary_tree_large.height() == 3

    t = BinaryTree(('first', 1))
    assert t.height() == 0
    t._root.left = Node('second', 2) # type: ignore
    assert t.height() == 1
    t._root.left.left = Node('fourth', 4) # type: ignore
    assert t.height() == 2
    t._root.left.right = Node('fifth', 5) # type: ignore
    assert t.height() == 2
    t._root.left.left = None # type: ignore
    t._root.left.right = None # type: ignore
    assert t.height() == 1
    t._root.left = None # type: ignore
    assert t.height() == 0
    t._root = None
    assert t.height() == -1


def test_binary_tree_copy(
    example_perfect_binary_tree_small: BinaryTree[str, int],
    example_perfect_binary_tree_medium: BinaryTree[str, int],
    example_perfect_binary_tree_large: BinaryTree[str, int],
):
    empty: BinaryTree = BinaryTree()
    empty_copy = empty.copy()
    assert empty is not empty_copy
    assert empty.height() == -1
    assert empty_copy.height() == -1

    for tree in (
        example_perfect_binary_tree_small,
        example_perfect_binary_tree_medium,
        example_perfect_binary_tree_large,
    ):
        copy = tree.copy()
        assert copy is not tree
        assert copy._root is not None and tree._root is not None
        assert copy._root is not tree._root
        assert copy._root.key == tree._root.key
        assert copy._root.value == tree._root.value
        assert copy.traverse_level_order() == tree.traverse_level_order()
        assert copy.traverse_pre_order() == tree.traverse_pre_order()
        assert copy.traverse_in_order() == tree.traverse_in_order()
        assert copy.traverse_post_order() == tree.traverse_post_order()
        assert copy.traverse_boundaries() == tree.traverse_boundaries()
        assert copy.height() == tree.height()
