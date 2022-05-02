from typing import Generic, Optional, Type, TypeVar

from ..utils import LinearNode as Node


DT = TypeVar('DT')

class Queue(Generic[DT]):
    def __init__(self, *args: DT):
        self._front: Optional[Node[DT]] = None
        self._rear: Optional[Node[DT]] = None

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
            self._front = Node(args[0])
            node: Optional[Node[DT]] = self._front
            counter = 0

            while node:
                try:
                    node.next = Node(args[counter + 1])
                except IndexError:
                    self._rear = node
                    node.next = None

                node = node.next
                counter += 1


    def __len__(self) -> int:
        count = 0
        node = self._front

        while node:
            count += 1
            node = node.next

        return count


    def __repr__(self) -> str:
        nodes: list[DT] = []
        node = self._front

        while node:
            nodes.append(node.data)
            node = node.next

        return str(nodes)


    def copy(self) -> 'Queue[DT]':
        q: Queue[DT] = Queue()
        source_node = self._front

        if source_node:
            q.enqueue(source_node.data)
            new_node = q._front

            while new_node and source_node.next:
                new_node.next = Node(source_node.next.data)
                new_node = new_node.next
                source_node = source_node.next

            q._rear = new_node

        return q


    def enqueue(self, data: DT):
        if not self._data_type:
            self._data_type = type(data)
        elif not isinstance(data, self._data_type):
            raise TypeError(f"Value must be of type {self._data_type}!")

        if not self._rear:
            self._front = self._rear = Node(data)
        else:
            self._rear.next = Node(data)
            self._rear = self._rear.next


    def dequeue(self) -> DT:
        if not self._front:
            raise RuntimeError('Queue is empty!')

        node = self._front
        self._front = node.next

        if not self._front:
            self._rear = self._front

        return node.data


    def front(self) -> DT:
        if not self._front:
            raise RuntimeError('Queue is empty!')

        return self._front.data


    def rear(self) -> DT:
        if not self._rear:
            raise RuntimeError('Queue is empty!')

        return self._rear.data


    def is_empty(self) -> bool:
        return not self._front and not self._rear

