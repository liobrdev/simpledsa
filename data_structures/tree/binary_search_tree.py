from math import ceil, floor
from typing import Generic, Optional, Type, TypeVar

from ..utils import BinaryTreeNode


VT = TypeVar('VT')


class BSTData(Generic[VT]):
    def __init__(
        self,
        key: bytes | float | int | str,
        value: Optional[VT] = None,
    ):
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return str({ 'key': self.key, 'value': self.value })


class Node(Generic[VT], BinaryTreeNode[BSTData]):
    def __init__(
        self,
        key: bytes | float | int | str,
        value: Optional[VT] = None,
    ):
        self.data = BSTData(key, value)
        self.left: Optional['Node[VT]'] = None
        self.right: Optional['Node[VT]'] = None


class BinarySearchTree(Generic[VT]):
    def __init__(
        self,
        *args: tuple[bytes | float | int | str, Optional[VT]],
        **kwargs
    ):
        self.__root: Optional[Node[VT]] = None

        if not args:
            self.__key_type = None
            self.__value_type = None
        else:
            self.__key_type, self.__value_type = self._check_data_types(*args)
            self.__construct_tree(*args, **kwargs)


    def _check_data_types(
        self,
        *args: tuple[bytes | float | int | str, Optional[VT]],
    ) -> (
        tuple[
            Optional[Type[bytes] | Type[float] | Type[int] | Type[str]],
            Optional[Type[VT]],]
    ):
        key_type: (
            Optional[Type[bytes] | Type[float] | Type[int] | Type[str]]
        ) = None
        value_type: Optional[Type[VT]] = None

        for arg in args:
            if not isinstance(arg, tuple):
                raise TypeError('All arguments must be key-value tuples!')

            if not isinstance(arg[0], (bytes, float, int, str)):
                raise TypeError(
                    "Keys must be of type 'bytes', 'float', 'int', or 'str'!",)
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


    def __construct_tree(
        self,
        *args: tuple[bytes | float | int | str, Optional[VT]],
    ):
        if not args:
            return

        data = sorted(args)

        if not self._is_valid_bst_in_order(*data):
            raise ValueError(
                'Cannot construct valid binary search tree ' +
                'from provided sequence - remove duplicate keys!',)

        root_min = 0
        root_max = len(data) - 1
        root_index = ceil((root_max + root_min) / 2)

        self.__root = Node(data[root_index][0], data[root_index][1])

        class QueueItem:
            def __init__(self, node: Node[VT], index: int, min: int, max: int):
                self.node = node
                self.index = index
                self.min = min
                self.max = max
        
        queue: list[QueueItem] = \
            [QueueItem(self.__root, root_index, root_min, root_max)]

        while queue:
            parent = queue.pop(0)

            if not parent.max > parent.min:
                continue

            if parent.index > parent.min:
                left_max = parent.index - 1
                left_index = ceil((left_max + parent.min) / 2)
                left_node = Node(data[left_index][0], data[left_index][1])
                parent.node.left = left_node
                queue.append(
                    QueueItem(left_node, left_index, parent.min, left_max),)

            if parent.index < parent.max:
                right_min = parent.index + 1
                right_index = floor((right_min + parent.max) / 2)
                right_node = Node(data[right_index][0], data[right_index][1])
                parent.node.right = right_node
                queue.append(
                    QueueItem(right_node, right_index, right_min, parent.max),)


    def _is_valid_bst_in_order(
        self,
        *args: tuple[bytes | float | int | str, Optional[VT]],
    ) -> bool:
        for index in range(len(args)):
            try:
                if not args[index][0] < args[index + 1][0]: # type: ignore
                    return False
            except IndexError:
                pass

        return True


    def __getitem__(self, key) -> Optional[VT]:
        if not self.__key_type:
            raise RuntimeError('Key type not defined!')
        elif not isinstance(key, self.__key_type):
            raise TypeError(f"Key must be of type {self.__key_type}!")

        current = self.__root

        while current:
            if key == current.data.key:
                return current.data.value

            if key < current.data.key: # type: ignore
                current = current.left
            elif key > current.data.key: # type: ignore
                current = current.right

        error_key = key

        if isinstance(key, str):
            error_key = f"'{key}'"

        raise KeyError(f"Key {error_key} not found!")


    def __setitem__(self, key, value: Optional[VT]):
        if not isinstance(key, (bytes, float, int, str)):
            raise TypeError('Invalid key!')

        if self.__key_type and not isinstance(key, self.__key_type):
            raise TypeError(f'Key must be of type {self.__key_type}!')

        if self.__value_type and not isinstance(value, self.__value_type):
            raise TypeError(f'Value must be of type {self.__value_type}!')

        if not self.__root:
            self.__key_type = type(key)

            if value is not None:
                self.__value_type = type(value)

            self.__root = Node(key, value)
            return

        current = self.__root

        while current:
            if key == current.data.key:
                current.data.value = value
                return
            elif key < current.data.key: # type: ignore
                if not current.left:
                    current.left = Node(key, value)
                    return
                else:
                    current = current.left
            elif key > current.data.key: # type: ignore
                if not current.right:
                    current.right = Node(key, value)
                    return
                else:
                    current = current.right


    def __delitem__(self, key):
        if not isinstance(key, (bytes, float, int, str)):
            raise TypeError('Invalid key!')

        if self.__key_type and not isinstance(key, self.__key_type):
            raise TypeError(f'Key must be of type {self.__key_type}!')

        current = self.__root
        parent: Optional[Node[VT]] = None

        while current:
            if key == current.data.key:
                if current.left and current.right:
                    successor_parent = current        
                    successor = current.right

                    while successor and successor.left:
                        successor_parent = successor
                        successor = successor.left

                    if successor_parent is not current:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right

                    current.data.key = successor.data.key
                    current.data.value = successor.data.value
                    return

                temp = None

                if current.left and not current.right:
                    temp = current.left
                elif current.right:
                    temp = current.right

                if parent:
                    if parent.left is current:
                        parent.left = temp
                    elif parent.right is current:
                        parent.right = temp
                else:
                    self.__root = temp
                return
            elif key < current.data.key: # type: ignore
                parent = current
                current = current.left
            elif key > current.data.key: # type: ignore
                parent = current
                current = current.right

        error_key = key

        if isinstance(key, str):
            error_key = f"'{key}'"

        raise KeyError(f"Key {error_key} not found!")


    def __len__(self) -> int:
        def count_nodes(root: Optional[Node[VT]]) -> int:
            if root:
                return 1 + count_nodes(root.left) + count_nodes(root.right)
            return 0
        
        return count_nodes(self.__root)


    def copy(self) -> 'BinarySearchTree[VT]':
        tree_copy: 'BinarySearchTree[VT]' = BinarySearchTree()

        if not self.__root:
            return tree_copy

        tree_copy.__key_type = self.__key_type
        tree_copy.__value_type = self.__value_type

        class QueueItem:
            def __init__(
                self,
                node: Node[VT],
                parent_copy: Optional[Node[VT]],
                position: Optional[bool],
            ):
                self.node = node
                self.parent_copy = parent_copy
                self.position = position

        queue: list[QueueItem] = [QueueItem(self.__root, None, None)]

        while queue:
            item = queue.pop(0)

            node_copy: Node[VT] = \
                Node(item.node.data.key, item.node.data.value)

            if item.parent_copy:
                if item.position is False:
                    item.parent_copy.left = node_copy
                elif item.position is True:
                    item.parent_copy.right = node_copy
            elif item.node is self.__root:
                tree_copy.__root = node_copy

            if item.node.left:
                queue.append(QueueItem(item.node.left, node_copy, False))

            if item.node.right:
                queue.append(QueueItem(item.node.right, node_copy, True))

        return tree_copy


    def height(self) -> int:
        height: int = -1

        if not self.__root:
            return height

        current_level: list[Node[VT]] = [self.__root]

        while current_level:
            height += 1
            next_level: list[Node[VT]] = []

            while current_level:
                current_node = current_level.pop(0)

                if current_node.left:
                    next_level.append(current_node.left)

                if current_node.right:
                     next_level.append(current_node.right)

            current_level = next_level

        return height


    def get(self, key) -> Optional[VT]:
        return self.__getitem__(key)


    def put(self, key, value: Optional[VT]):
        self.__setitem__(key, value)


    def remove(self, key):
        self.__delitem__(key)


    def traverse_level_order(self) -> (
        list[tuple[bytes | float | int | str, Optional[VT]]]
    ):
        if not self.__root:
            return []

        nodes: list[tuple[bytes | float | int | str, Optional[VT]]] = []
        queue: list[Node[VT]] = [self.__root]

        while queue:
            current = queue.pop(0)
            nodes.append((current.data.key, current.data.value))

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return nodes


    def traverse_pre_order(self) -> (
        list[tuple[bytes | float | int | str, Optional[VT]]]
    ):
        def traverse(
            root: Optional[Node[VT]],
            nodes: list[tuple[bytes | float | int | str, Optional[VT]]],
        ):
            if root:
                nodes.append((root.data.key, root.data.value))
                traverse(root.left, nodes)
                traverse(root.right, nodes)

            return nodes

        return traverse(self.__root, [])


    def traverse_in_order(self) -> (
        list[tuple[bytes | float | int | str, Optional[VT]]]
    ):
        def traverse(
            root: Optional[Node[VT]],
            nodes: list[tuple[bytes | float | int | str, Optional[VT]]],
        ):
            if root:
                traverse(root.left, nodes)
                nodes.append((root.data.key, root.data.value))
                traverse(root.right, nodes)

            return nodes

        return traverse(self.__root, [])


    def traverse_post_order(self) -> (
        list[tuple[bytes | float | int | str, Optional[VT]]]
    ):
        def traverse(
            root: Optional[Node[VT]],
            nodes: list[tuple[bytes | float | int | str, Optional[VT]]],
        ):
            if root:
                traverse(root.left, nodes)
                traverse(root.right, nodes)
                nodes.append((root.data.key, root.data.value))

            return nodes

        return traverse(self.__root, [])

