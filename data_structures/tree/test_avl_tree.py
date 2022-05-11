from . import AVLTree as AVL


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

