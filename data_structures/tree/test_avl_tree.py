from . import AVLTree as AVL
from ..utils import AVLTreeNode as Node


def test_avl_tree_copy(
    example_perfect_avl_small: AVL[str],
    example_perfect_avl_medium: AVL[str],
    example_perfect_avl_large: AVL[str],
):
    empty: AVL = AVL()
    empty_copy = empty.copy()
    assert empty is not empty_copy
    assert empty.height() == -1
    assert empty_copy.height() == -1

    for tree in (
        example_perfect_avl_small,
        example_perfect_avl_medium,
        example_perfect_avl_large,
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


def test_avl_get_node_heights(
    example_perfect_avl_small: AVL[str],
    example_perfect_avl_medium: AVL[str],
    example_perfect_avl_large: AVL[str],
):
    assert example_perfect_avl_small._get_node_heights() == [
        {'height': 0, 'key': 1}, {'height': 1, 'key': 2},
        {'height': 0, 'key': 3},]

    assert example_perfect_avl_medium._get_node_heights() == [
        {'height': 0, 'key': 1}, {'height': 1, 'key': 2},
        {'height': 0, 'key': 3}, {'height': 2, 'key': 4},
        {'height': 0, 'key': 5}, {'height': 1, 'key': 6},
        {'height': 0, 'key': 7},]

    assert example_perfect_avl_large._get_node_heights() == [
        {'height': 0, 'key': 1}, {'height': 1, 'key': 2},
        {'height': 0, 'key': 3}, {'height': 2, 'key': 4},
        {'height': 0, 'key': 5}, {'height': 1, 'key': 6},
        {'height': 0, 'key': 7}, {'height': 3, 'key': 8},
        {'height': 0, 'key': 9}, {'height': 1, 'key': 10},
        {'height': 0, 'key': 11}, {'height': 2, 'key': 12},
        {'height': 0, 'key': 13}, {'height': 1, 'key': 14},
        {'height': 0, 'key': 15},]


def test_avl_find_height_inbalance(
    example_perfect_avl_small: AVL[str],
    example_perfect_avl_medium: AVL[str],
    example_perfect_avl_large: AVL[str],
):
    assert example_perfect_avl_small.find_height_inbalance() is None
    assert example_perfect_avl_medium.find_height_inbalance() is None
    assert example_perfect_avl_large.find_height_inbalance() is None

    tree: AVL[str] = example_perfect_avl_small.copy()
    assert tree._get_node_heights() == [
        {'height': 0, 'key': 1}, {'height': 1, 'key': 2},
        {'height': 0, 'key': 3},]
    assert tree._root is not None
    assert tree._root.left is not None
    assert tree._root.left.left is None
    assert tree.find_height_inbalance() is None

    tree._root.left.left = Node(0, 'zero')
    tree._root.left.height += 1
    tree._root.height += 1
    assert tree.find_height_inbalance() is None

    tree._root.left.left.left = Node(-1, 'minus_one')
    tree._root.left.left.height += 1
    tree._root.left.height += 1
    tree._root.height += 1
    assert tree.find_height_inbalance() == \
        {'key': 1, 'left_height': 1, 'right_height': -1}

    tree._root.left.left.left = None
    tree._root.left.left.height -= 1
    tree._root.left.height -= 1
    tree._root.height -= 1
    assert tree.find_height_inbalance() is None

    tree._root.right = None
    assert tree.find_height_inbalance() == \
        {'key': 2, 'left_height': 1, 'right_height': -1}

