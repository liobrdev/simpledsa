from typing import Generic, Optional, Type, TypeVar

from ..utils import LinearNode as Node


DT = TypeVar('DT')

class LinkedList(Generic[DT]):
    def __init__(self, *args: DT):
        self._head: Optional[Node[DT]] = None

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
            self._head = Node(args[0])
            node: Optional[Node[DT]] = self._head
            counter = 0

            while node:
                try:
                    node.next = Node(args[counter + 1])
                except IndexError:
                    node.next = None

                node = node.next
                counter += 1


    def __add__(self, other: object) -> 'LinkedList':
        if not isinstance(other, (type(self), list, tuple)):
            raise TypeError(
                'Unsupported operand type(s) for +:' +
                f" '{type(self)}' and '{type(other)}'")
        elif isinstance(other, (list, tuple)):
            if not other:
                return self.copy()

            source_node = self._head

            if not source_node:
                return LinkedList(*other)

            for item in other:
                if type(item) != type(source_node.data):
                    raise TypeError(
                        'Appended items must be of type' +
                        f" '{type(source_node.data)}'")

            l = self.copy()
            node = l._head

            while node and node.next:
                node = node.next

            index = 0

            while node:
                try:
                    node.next = Node(other[index])
                except IndexError:
                    break

                node = node.next
                index += 1

            return l
        else:
            if self._head and not other._head:
                return self.copy()
            elif not self._head and other._head:
                return other.copy()
            elif not self._head and not other._head:
                return LinkedList()
            else:
                if self._data_type is not other._data_type:
                    raise TypeError(
                        'Cannot merge linked lists with different data types:' +
                        f" '{self._data_type}' and '{other._data_type}'")

                l = self.copy()
                node = l._head

                while node and node.next:
                    node = node.next

                other_node = other._head

                while node and other_node:
                    node.next = Node(other_node.data)
                    node = node.next
                    other_node = other_node.next

                return l


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False

        first = self._head
        second = other._head

        if not first and not second:
            return True

        while first:
            if not second or first.data != second.data:
                return False

            first = first.next
            second = second.next

        return True


    def __len__(self) -> int:
        count = 0
        node = self._head

        while node:
            count += 1
            node = node.next

        return count


    def __repr__(self) -> str:
        nodes: list[DT] = []
        node = self._head

        while node:
            nodes.append(node.data)
            node = node.next

        return str(nodes)


    def append(self, data: DT):
        if not self._data_type:
            self._data_type = type(data)
        elif not isinstance(data, self._data_type):
            raise TypeError(f"Value must be of type {self._data_type}!")

        previous = None
        current = self._head

        while current:
            previous = current
            current = current.next

        node = Node(data, current)

        if previous:
            previous.next = node
        else:
            self._head = node


    def copy(self) -> 'LinkedList[DT]':
        l: LinkedList[DT] = LinkedList()
        source_node = self._head

        if source_node:
            l.append(source_node.data)
            new_node = l._head

            while new_node and source_node.next:
                new_node.next = Node(source_node.next.data)
                new_node = new_node.next
                source_node = source_node.next

        return l


    def delete(self, data: DT):
        previous = None
        current = self._head

        while current:
            if current.data == data:
                if previous:
                    next = current.next
                    previous.next = next
                else:
                    self._head = current.next

                del current
                return

            previous = current
            current = current.next

        raise ValueError(f"'{data}' is not in linked list!")


    def find(self, data: DT) -> dict[str, DT | str | int]:
        current = self._head
        counter = 0

        while current:
            if current.data == data:
                return {
                    'data': current.data,
                    'index': counter,
                    'node': hex(id(current)),
                }

            current = current.next
            counter += 1

        raise ValueError(f"'{data}' is not in linked list!")


    def insert(self, data: DT, index: int = 0):
        if not self._data_type:
            self._data_type = type(data)
        elif not isinstance(data, self._data_type):
            raise TypeError(f"Value must be of type {self._data_type}!")

        if not isinstance(index, int):
            raise TypeError('Index must be an integer!')

        if index < 0:
            raise IndexError('LinkedList index out of range!')
        else:
            previous = None
            current = self._head
            counter = 0

            while current:
                if counter == index:
                    break

                previous = current
                current = current.next
                counter += 1

            node = Node(data, current)

            if previous:
                previous.next = node
            else:
                self._head = node


    def reverse(self):
        previous = None
        current = self._head

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self._head = previous


    def traverse(self):
        if not self._head:
            return print('No HEAD node.')

        index = 0
        current = self._head

        while current:
            if current is self._head:
                print('Index 0 (HEAD)')
            else:
                print(f'Index {index}')

            print(current)

            if not current.next:
                return print('End of linked list.')

            try:
                value = input('Press Enter to view NEXT node (^C to exit):\n')
            except KeyboardInterrupt:
                return

            if value.lower().strip() in ['', 'enter', 'next']:
                index += 1
                current = current.next
            elif value.lower().strip() in ['^c', 'exit', 'cancel']:
                return


    def update(self, data: DT, value: DT):
        current = self._head

        while current:
            if current.data == data:
                current.data = value
                return

            current = current.next

        raise ValueError(f"'{data}' is not in linked list!")

