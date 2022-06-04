from .infinite_string import InfiniteString
from .nodes import LinearNode, BinaryTreeNode
from .prime_numbers import is_prime, next_prime


INF_NUM = float('inf')
INF_STR = InfiniteString()


def flatten(items: list):
    try:
        for index, item in enumerate(items):
            while isinstance(item, list):    
                items[index:index + 1] = item
                item = items[index]
    except IndexError:
        pass
    return items


__all__ = [
    'LinearNode', 'BinaryTreeNode',
    'INF_NUM', 'INF_STR',
    'flatten', 'is_prime', 'next_prime',]
