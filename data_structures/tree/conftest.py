from pytest import fixture

from .binary_search_tree import BinarySearchTree


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

