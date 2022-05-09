from typing import Generic, Optional, Type, TypeVar

from ..queue import Queue
from ..stack import Stack
from ..utils import BinaryTreeNode as Node


KT = TypeVar('KT')
VT = TypeVar('VT')


class BinaryTree(Generic[KT, VT]):
    def __init__(self, *args: tuple[KT, Optional[VT]]):
        self._root: Optional[Node[KT, VT]] = None

        if not args:
            self._key_type = None
            self._value_type = None
        else:
            self._key_type, self._value_type = self._check_data_types(*args)
            self._construct_tree(*args)


    def _check_data_types(
        self, *args: tuple[KT, Optional[VT]],
    ) -> tuple[Optional[Type[KT]], Optional[Type[VT]]]:
        key_type: Optional[Type[KT]] = None
        value_type: Optional[Type[VT]] = None

        for index, arg in enumerate(args):
            if not isinstance(arg, tuple):
                raise TypeError('All arguments must be key-value tuples!')

            if arg[0] is None:
                raise TypeError('Keys must not be None!')
            elif not isinstance(arg[0], type(args[index - 1][0])):
                raise TypeError('All keys must have the same type!')
            else:
                key_type = type(arg[0])

            if arg[1] is None:
                pass
            elif not value_type:
                value_type = type(arg[1])
            elif not isinstance(arg[1], value_type):
                raise TypeError('All values must have the same type!')

        return key_type, value_type


    def _construct_tree(self, *args: tuple[KT, Optional[VT]]):
        if args:
            nodes = [Node(key, value) for key, value in args]

            self._root = nodes[0]

            for index, node in enumerate(nodes):
                try:
                    node.left = nodes[index * 2 + 1]
                    node.right = nodes[index * 2 + 2]
                except IndexError:
                    break


    def __len__(self) -> int:
        count: int = 0
        ancestors: Stack[Node[KT, VT]] = Stack()
        previous: Optional[Node[KT, VT]] = None
        current: Optional[Node[KT, VT]] = self._root

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

            count += 1

            previous = current

            try:
                current = ancestors.pop()
            except RuntimeError:
                current = None

        return count


    def traverse_level_order(self) -> list[tuple[KT, Optional[VT]]]:
        if not self._root:
            return []

        nodes: list[tuple[KT, Optional[VT]]] = []
        queue: Queue[Node[KT, VT]] = Queue(self._root)

        while not queue.is_empty():
            current = queue.dequeue()
            nodes.append((current.key, current.value))

            if current.left:
                queue.enqueue(current.left)

            if current.right:
                queue.enqueue(current.right)

        return nodes


    def traverse_pre_order(self) -> list[tuple[KT, Optional[VT]]]:
        nodes: list[tuple[KT, Optional[VT]]] = []
        ancestors: Stack[Node[KT, VT]] = Stack()
        previous: Optional[Node[KT, VT]] = None
        current: Optional[Node[KT, VT]] = self._root

        while current:
            try:
                parent = ancestors.top()
            except RuntimeError:
                parent = None

            if previous is parent:
                nodes.append((current.key, current.value))

                if current.left:
                    ancestors.push(current)
                    previous = current
                    current = current.left
                    continue

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

        return nodes


    def traverse_in_order(self) -> list[tuple[KT, Optional[VT]]]:
        nodes: list[tuple[KT, Optional[VT]]] = []
        ancestors: Stack[Node[KT, VT]] = Stack()
        previous: Optional[Node[KT, VT]] = None
        current: Optional[Node[KT, VT]] = self._root

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
                nodes.append((current.key, current.value))

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

        return nodes


    def traverse_post_order(self) -> list[tuple[KT, Optional[VT]]]:
        nodes: list[tuple[KT, Optional[VT]]] = []
        ancestors: Stack[Node[KT, VT]] = Stack()
        previous: Optional[Node[KT, VT]] = None
        current: Optional[Node[KT, VT]] = self._root

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

            nodes.append((current.key, current.value))

            previous = current

            try:
                current = ancestors.pop()
            except RuntimeError:
                current = None

        return nodes


    def traverse_boundaries(self) -> list[tuple[KT, Optional[VT]]]:
        nodes: list[tuple[KT, Optional[VT]]] = []
        ancestors: Stack[Node[KT, VT]] = Stack()
        previous: Optional[Node[KT, VT]] = None
        current: Optional[Node[KT, VT]] = self._root

        while current and current.right:
            current = current.right
        
        right_corner = current
        traversing_left = True
        traversing_right = False

        current = self._root

        while current:
            try:
                parent = ancestors.top()
            except RuntimeError:
                parent = None
            
            if current is right_corner:
                traversing_left = False
                traversing_right = True

            if previous is parent:
                if traversing_left:
                    nodes.append((current.key, current.value))

                if current.left:
                    ancestors.push(current)
                    previous = current
                    current = current.left
                    continue

            if current.right and previous is not current.right:
                ancestors.push(current)
                previous = current
                current = current.right
                continue

            if (
                not current.left and not current.right
                or traversing_right and current is not self._root
            ):
                if not traversing_left:
                    nodes.append((current.key, current.value))

                traversing_left = False

            previous = current

            try:
                current = ancestors.pop()
            except RuntimeError:
                current = None

        return nodes


    def height(self) -> int:
        height: int = -1

        if not self._root:
            return height

        queue: Queue[Stack[Node[KT, VT]]] = Queue(Stack(self._root))

        while not queue.is_empty():
            height += 1

            current_stack = queue.dequeue()
            next_stack: Stack[Node[KT, VT]] = Stack()

            while not current_stack.is_empty():
                current_node = current_stack.pop()

                if current_node.left:
                    next_stack.push(current_node.left)

                if current_node.right:
                     next_stack.push(current_node.right)

            if not next_stack.is_empty():
                queue.enqueue(next_stack)

        return height

