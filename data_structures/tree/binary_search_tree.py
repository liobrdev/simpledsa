from math import ceil, floor
from typing import Optional, Type, TypeVar

from . import BinaryTree
from ..queue import Queue
from ..stack import Stack
from ..utils import BinaryTreeNode as Node, INF_NUM, INF_STR


VT = TypeVar('VT')

class BinarySearchTree(BinaryTree[int | float | str, VT]):
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


    def _check_data_types(
        self, *args: tuple[int | float | str, Optional[VT]],
    ) -> tuple[Optional[Type[int | float | str]], Optional[Type[VT]]]:
        key_type: Optional[Type[int | float | str]] = None
        value_type: Optional[Type[VT]] = None

        for arg in args:
            if not isinstance(arg, tuple):
                raise TypeError('All arguments must be key-value tuples!')

            if not isinstance(arg[0], (int, float, str)):
                raise TypeError(
                    "Keys must be of type 'int', 'float', or 'str'!",)
            elif not key_type:
                key_type = type(arg[0])
            elif not isinstance(arg[0], key_type):
                raise TypeError('All keys must have the same type!')

            if arg[1] is None:
                pass
            elif not value_type:
                value_type = type(arg[1])
            elif not isinstance(arg[1], value_type):
                raise TypeError('All values must have the same type!')

        return key_type, value_type


    def _construct_tree(
        self, *args: tuple[int | float | str, Optional[VT]], **kwargs,
    ):
        if args:
            if kwargs.get('level_order') is True:
                if self._is_valid_bst_level_order(*args):
                    self._construct_from_level_order(*args)
                else:
                    raise ValueError(
                        'Cannot construct valid binary search tree ' +
                        'from provided level-order sequence!',)
            elif kwargs.get('pre_order') is True:
                if self._is_valid_bst_pre_order(*args):
                    self._construct_from_pre_order(*args)
                else:
                    raise ValueError(
                        'Cannot construct valid binary search tree ' +
                        'from provided pre-order sequence!',)
            elif kwargs.get('in_order') is True:
                if self._is_valid_bst_in_order(*args):
                    self._construct_from_in_order(*args)
                else:
                    raise ValueError(
                        'Cannot construct valid binary search tree ' +
                        'from provided in-order sequence!',)
            elif kwargs.get('post_order') is True:
                if self._is_valid_bst_post_order(*args):
                    self._construct_from_post_order(*args)
                else:
                    raise ValueError(
                        'Cannot construct valid binary search tree ' +
                        'from provided post-order sequence!',)
            else:
                sorted_args = sorted(args)

                if self._is_valid_bst_in_order(*sorted_args):
                    self._construct_from_in_order(*sorted_args)
                else:
                    raise ValueError(
                        'Cannot construct valid binary search tree ' +
                        'from provided sequence - remove duplicate values!',)


    def _is_valid_bst_level_order(
        self, *args: tuple[int | float | str, Optional[VT]],
    ) -> bool:
        if not args:
            return True

        min: int | float | str = -INF_NUM
        max: int | float | str = INF_NUM

        if self._key_type is type(str):
            min = -INF_STR
            max = INF_STR

        keys = [arg[0] for arg in args]
        q: Queue[dict[str, int | float | str]] = \
            Queue({ 'key': keys[0], 'min': min, 'max': max })

        index = 1

        while index < len(keys) and not q.is_empty():
            parent = q.dequeue()

            if (
                index < len(keys)
                and keys[index] < parent['key'] # type: ignore
                and parent['min'] < keys[index] # type: ignore
            ):
                q.enqueue({
                    'key': keys[index],
                    'min': parent['min'],
                    'max': parent['key'],
                })

                index += 1

            if (
                index < len(keys)
                and keys[index] > parent['key'] # type: ignore
                and parent['max'] > keys[index] # type: ignore
            ):
                q.enqueue({
                    'key': keys[index],
                    'min': parent['key'],
                    'max': parent['max'],
                })

                index += 1

        if index == len(keys):
            return True

        return False


    def _is_valid_bst_pre_order(
        self, *args: tuple[int | float | str, Optional[VT]],
    ) -> bool:
        if not args:
            return True

        parent_key: int | float | str = -INF_NUM

        if self._key_type is type(str):
            parent_key = -INF_STR

        keys = [arg[0] for arg in args]
        ancestors: Stack[int | float | str] = Stack()

        for key in keys:
            if parent_key > key: # type: ignore
                return False

            while (
                not ancestors.is_empty()
                and ancestors.top() < key # type: ignore
            ):
                parent_key = ancestors.pop()

            ancestors.push(key)

        return True


    def _is_valid_bst_in_order(
        self, *args: tuple[int | float | str, Optional[VT]],
    ) -> bool:
        for index in range(len(args)):
            try:
                if not args[index][0] < args[index + 1][0]: # type: ignore
                    return False
            except IndexError:
                pass

        return True


    def _is_valid_bst_post_order(
        self, *args: tuple[int | float | str, Optional[VT]],
    ) -> bool:
        if not args:
            return True

        parent_key: int | float | str = INF_NUM

        if self._key_type is type(str):
            parent_key = INF_STR

        keys = [arg[0] for arg in args]
        ancestors: Stack[int | float | str] = Stack()
        index = len(keys) - 1

        while index >= 0:
            key = keys[index]

            if parent_key < key: # type: ignore
                return False

            while (
                not ancestors.is_empty()
                and ancestors.top() > key # type: ignore
            ):
                parent_key = ancestors.pop()

            ancestors.push(key)
            index -= 1

        return True


    def _construct_from_level_order(
        self, *args: tuple[int | float | str, Optional[VT]],
    ):
        if not args:
            return

        min: int | float | str = -INF_NUM
        max: int | float | str = INF_NUM

        if self._key_type is type(str):
            min = -INF_STR
            max = INF_STR

        data = list(args)
        self._root = Node(data[0][0], data[0][1])

        class QueueItem:
            def __init__(
                self,
                node: Node[int | float | str, VT],
                min: int | float | str,
                max: int | float | str,
            ):
                self.node, self.min, self.max = node, min, max

        q: Queue[QueueItem] = Queue(QueueItem(self._root, min, max))

        index = 1

        while index < len(data) and not q.is_empty():
            parent = q.dequeue()

            if (
                index < len(data)
                and data[index][0] < parent.node.key # type: ignore
                and parent.min < data[index][0] # type: ignore
            ):
                left_child = Node(data[index][0], data[index][1])
                parent.node.left = left_child
                q.enqueue(QueueItem(left_child, parent.min, parent.node.key))
                index += 1

            if (
                index < len(data)
                and data[index][0] > parent.node.key # type: ignore
                and parent.max > data[index][0] # type: ignore
            ):
                right_child = Node(data[index][0], data[index][1])
                parent.node.right = right_child
                q.enqueue(QueueItem(right_child, parent.node.key, parent.max))
                index += 1


    def _construct_from_pre_order(
        self, *args: tuple[int | float | str, Optional[VT]],
    ):
        if not args:
            return

        data = list(args)
        self._root = Node(data[0][0], data[0][1])
        ancestors: Stack[Node[int | float | str, VT]] = Stack(self._root)

        for datum in data[1:]:
            parent: Optional[Node[int | float | str, VT]] = None

            while (
                not ancestors.is_empty()
                and datum[0] > ancestors.top().key # type: ignore
            ):
                parent = ancestors.pop()

            if parent:
                parent.right = Node(datum[0], datum[1])
                ancestors.push(parent.right)
            else:
                parent = ancestors.top()
                parent.left = Node(datum[0], datum[1])
                ancestors.push(parent.left)


    def _construct_from_in_order(
        self, *args: tuple[int | float | str, Optional[VT]],
    ):
        if not args:
            return

        data = list(args)
        root_min = 0
        root_max = len(data) - 1
        root_index = ceil((root_max + root_min) / 2)
        self._root = Node(data[root_index][0], data[root_index][1])

        class QueueItem:
            def __init__(
                self,
                node: Node[int | float | str, VT],
                index: int, min: int, max: int,
            ):
                self.node = node
                self.index, self.min, self.max = index, min, max
        
        q: Queue[QueueItem] = \
            Queue(QueueItem(self._root, root_index, root_min, root_max))

        while not q.is_empty():
            parent = q.dequeue()

            if not parent.max > parent.min:
                continue

            if parent.index > parent.min:
                left_max = parent.index - 1
                left_index = ceil((left_max + parent.min) / 2)
                left_node = Node(data[left_index][0], data[left_index][1])
                parent.node.left = left_node
                q.enqueue(
                    QueueItem(left_node, left_index, parent.min, left_max),)

            if parent.index < parent.max:
                right_min = parent.index + 1
                right_index = floor((right_min + parent.max) / 2)
                right_node = Node(data[right_index][0], data[right_index][1])
                parent.node.right = right_node
                q.enqueue(
                    QueueItem(right_node, right_index, right_min, parent.max),)


    def _construct_from_post_order(
        self, *args: tuple[int | float | str, Optional[VT]],
    ):
        if not args:
            return

        data = list(args)
        self._root = Node(data[-1][0], data[-1][1])
        ancestors: Stack[Node[int | float | str, VT]] = Stack(self._root)

        index = len(data) - 2

        while index >= 0:
            datum = data[index]
            parent: Optional[Node[int | float | str, VT]] = None

            while (
                not ancestors.is_empty()
                and datum[0] < ancestors.top().key # type: ignore
            ):
                parent = ancestors.pop()

            if parent:
                parent.left = Node(datum[0], datum[1])
                ancestors.push(parent.left)
            else:
                parent = ancestors.top()
                parent.right = Node(datum[0], datum[1])
                ancestors.push(parent.right)

            index -= 1


    def __getitem__(self, key: int | float | str) -> Optional[VT]:
        if not self._key_type:
            raise RuntimeError('Key type not defined!')
        elif not isinstance(key, self._key_type):
            raise TypeError(f"Key must be of type {self._key_type}!")

        current = self._root

        while current:
            if key == current.key:
                return current.value

            if key < current.key: # type: ignore
                current = current.left
            elif key > current.key: # type: ignore
                current = current.right

        error_key = key

        if isinstance(key, str):
            error_key = f"'{key}'"

        raise KeyError(f"Key {error_key} not found!")


    def __setitem__(self, key: int | float | str, value: Optional[VT]):
        if not isinstance(key, (int, float, str)):
            raise TypeError('Invalid key!')

        if self._key_type and not isinstance(key, self._key_type):
            raise TypeError(f'Key must be of type {self._key_type}!')

        if self._value_type and not isinstance(value, self._value_type):
            raise TypeError(f'Value must be of type {self._value_type}!')

        if not self._root:
            self._key_type = type(key)

            if value is not None:
                self._value_type = type(value)

            self._root = Node(key, value)
            return

        current = self._root

        while current:
            if key == current.key:
                current.value = value
                return

            if key < current.key: # type: ignore
                if not current.left:
                    current.left = Node(key, value)
                    return
                else:
                    current = current.left
            elif key > current.key: # type: ignore
                if not current.right:
                    current.right = Node(key, value)
                    return
                else:
                    current = current.right


    def __delitem__(self, key: int | float | str):
        if not isinstance(key, (int, float, str)):
            raise TypeError('Invalid key!')

        if self._key_type and not isinstance(key, self._key_type):
            raise TypeError(f'Key must be of type {self._key_type}!')

        current = self._root
        parent: Optional[Node[int | float | str, VT]] = None

        while current:
            if key == current.key:
                if parent:
                    if parent.left is current:
                        parent.left = None
                    elif parent.right is current:
                        parent.right = None
                else:
                    self._root = None

                del current
                return

            parent = current

            if key < current.key: # type: ignore
                current = current.left
            elif key > current.key: # type: ignore
                current = current.right

        error_key = key

        if isinstance(key, str):
            error_key = f"'{key}'"

        raise KeyError(f"Key {error_key} not found!")


    def copy(self) -> 'BinarySearchTree[VT]':
        tree_copy: 'BinarySearchTree[VT]' = BinarySearchTree()

        if not self._root:
            return tree_copy

        return self._helper_copy_tree(tree_copy, Node)


    def get(self, key: int | float | str) -> Optional[VT]:
        return self.__getitem__(key)


    def put(self, key: int | float | str, value: Optional[VT]):
        self.__setitem__(key, value)


    def remove(self, key: int | float | str):
        self.__delitem__(key)

