from typing import Optional, TypeVar

from . import BinarySearchTree
from ..stack import Stack
from ..utils import AVLTreeNode as Node


VT = TypeVar('VT')

class AVLTree(BinarySearchTree[VT]):
    def __init__(
        self, *args: tuple[int | float | str, Optional[VT]], **kwargs,
    ):
        self._root: Optional[Node[int | float | str, VT]] = None

        if not args:
            self._key_type = None
            self._value_type = None
        else:
            self._key_type, self._value_type = self._check_data_types(*args)
            self._construct_tree(*args, **kwargs)
            self._set_node_heights()


    def _set_node_heights(self):
        ancestors: Stack[Node[int | float | str, VT]] = Stack()
        previous: Optional[Node[int | float | str, VT]] = None
        current: Optional[Node[int | float | str, VT]] = self._root

        while current:
            try:
                parent = ancestors.top()
            except RuntimeError:
                parent = None

            if current.left and previous is parent:
                ancestors.push(current)
                previous = current
                current = current.left
                continue

            if current.right and (
                current.left and previous is current.left
                or not current.left and previous is parent
            ):
                ancestors.push(current)
                previous = current
                current = current.right
                continue

            if not current.left and not current.right:
                current.height = 0
            elif current.left and not current.right:
                current.height = current.left.height + 1
            elif current.right and not current.left:
                current.height = current.right.height + 1
            else:
                current.height = \
                    max(current.left.height, current.right.height) + 1

            previous = current

            try:
                current = ancestors.pop()
            except RuntimeError:
                current = None


    def _get_node_heights(self) -> list[dict[str, int | float | str]]:
        heights: list[dict[str, int | float | str]] = []
        ancestors: Stack[Node[int | float | str, VT]] = Stack()
        previous: Optional[Node[int | float | str, VT]] = None
        current: Optional[Node[int | float | str, VT]] = self._root

        while current:
            try:
                parent = ancestors.top()
            except RuntimeError:
                parent = None

            if current.left and previous is parent:
                ancestors.push(current)
                previous = current
                current = current.left
                continue

            if (
                current.left and previous is current.left
                or not current.left and previous is parent
            ):
                heights.append(dict(key=current.key, height=current.height))

            if current.right and previous is not current.right:
                ancestors.push(current)
                previous = current
                current = current.right
                continue

            previous = current

            try:
                current = ancestors.pop()
            except RuntimeError:
                current = None

        return heights


    def copy(self) -> 'AVLTree[VT]':
        tree_copy: 'AVLTree[VT]' = AVLTree()

        if not self._root:
            return tree_copy

        tree_copy = self._helper_copy_tree(tree_copy, Node)
        tree_copy._set_node_heights()
        return tree_copy


    def find_height_inbalance(self) -> Optional[dict[str, int | float | str]]:
        ancestors: Stack[Node[int | float | str, VT]] = Stack()
        previous: Optional[Node[int | float | str, VT]] = None
        current: Optional[Node[int | float | str, VT]] = self._root

        while current:
            try:
                parent = ancestors.top()
            except RuntimeError:
                parent = None

            if current.left and previous is parent:
                ancestors.push(current)
                previous = current
                current = current.left
                continue

            if current.right and (
                current.left and previous is current.left
                or not current.left and previous is parent
            ):
                ancestors.push(current)
                previous = current
                current = current.right
                continue

            left_height: int = -1
            right_height: int = -1

            if current.left:
                left_height = current.left.height
            
            if current.right:
                right_height = current.right.height

            if not abs(left_height - right_height) <= 1:
                return dict(
                    key=current.key, left_height=left_height,
                    right_height=right_height,)

            previous = current

            try:
                current = ancestors.pop()
            except RuntimeError:
                current = None

        return None

