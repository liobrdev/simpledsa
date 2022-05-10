from typing import Generic, Optional, Type, TypeVar

from ..utils import LinearNode as Node


DT = TypeVar('DT')

class Stack(Generic[DT]):
    def __init__(self, *args: DT):
        self._top: Optional[Node[DT]] = None

        if not args:
            self._data_type = None
        else:
            self._data_type = self._check_data_types(*args)
            self._connect_nodes(*args)


    def _check_data_types(self, *args: DT) -> Type[DT]:
        for index, data in enumerate(args):
            if not isinstance(data, type(args[index - 1])):
                raise TypeError('All entries must have the same type!')
        
        return type(args[0])


    def _connect_nodes(self, *args: DT):
        if args:
            counter = len(args) - 1
            self._top = Node(args[counter])
            node: Optional[Node[DT]] = self._top

            while node:
                if counter > 0:
                    node.next = Node(args[counter - 1])
                else:
                    node.next = None

                counter -= 1
                node = node.next


    def __len__(self) -> int:
        count = 0
        node = self._top

        while node:
            count += 1
            node = node.next

        return count


    def __repr__(self) -> str:
        nodes: list[DT] = []
        node = self._top

        while node:
            nodes.insert(0, node.data)
            node = node.next

        return str(nodes)


    def copy(self) -> 'Stack[DT]':
        s: Stack[DT] = Stack()
        source_node = self._top

        if source_node:
            s.push(source_node.data)
            new_node = s._top

            while new_node and source_node.next:
                new_node.next = Node(source_node.next.data)
                new_node = new_node.next
                source_node = source_node.next

        return s


    def push(self, data: DT):
        if not self._data_type:
            self._data_type = type(data)
        elif not isinstance(data, self._data_type):
            raise TypeError(f"Value must be of type {self._data_type}!")

        node = Node(data)
        node.next = self._top
        self._top = node


    def pop(self) -> DT:
        if not self._top:
            raise RuntimeError('Underflow - stack is empty!')

        node = self._top
        data = node.data
        self._top = node.next
        del node

        return data


    def top(self) -> DT:
        if not self._top:
            raise RuntimeError('Underflow - stack is empty!')

        return self._top.data


    def is_empty(self) -> bool:
        return not self._top

