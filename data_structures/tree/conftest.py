from pytest import fixture

from . import BinaryTree, BinarySearchTree


@fixture
def example_perfect_binary_tree_small() -> BinaryTree[str, int]:
    return BinaryTree(('first', 1), ('second', 2), ('third', 3))


@fixture
def example_perfect_binary_tree_medium() -> BinaryTree[str, int]:
    return BinaryTree(
        ('first', 1), ('second', 2), ('third', 3), ('fourth', 4), ('fifth', 5),
        ('sixth', 6), ('seventh', 7),)

@fixture
def example_perfect_binary_tree_large() -> BinaryTree[str, int]:
    return BinaryTree(
        ('first', 1), ('second', 2), ('third', 3), ('fourth', 4), ('fifth', 5),
        ('sixth', 6), ('seventh', 7), ('eighth', 8), ('ninth', 9),
        ('tenth', 10), ('eleventh', 11), ('twelfth', 12), ('thirteenth', 13),
        ('fourteenth', 14), ('fifteenth', 15),)


@fixture
def example_perfect_bst_small() -> BinarySearchTree[str]:
    return BinarySearchTree((1, 'first'), (2, 'second'), (3, 'third'))


@fixture
def example_perfect_bst_medium() -> BinarySearchTree[str]:
    return BinarySearchTree(
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'),)


@fixture
def example_perfect_bst_large() -> BinarySearchTree[str]:
    return BinarySearchTree(
        (1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),
        (6, 'sixth'), (7, 'seventh'), (8, 'eighth'), (9, 'ninth'),
        (10, 'tenth'), (11, 'eleventh'), (12, 'twelfth'), (13, 'thirteenth'),
        (14, 'fourteenth'), (15, 'fifteenth'),)
