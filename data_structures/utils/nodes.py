from typing import Generic, Optional, TypeVar


DT = TypeVar('DT')
KT = TypeVar('KT')
VT = TypeVar('VT')


class LinearNode(Generic[DT]):
    def __init__(
        self,
        data: DT,
        next: Optional['LinearNode[DT]'] = None,
    ):
        self.data = data
        self.next = next

    def __repr__(self):
        return str({
            'data': self.data,
            'address': hex(id(self)),
            'has_next': bool(self.next)
        })


class BinaryTreeNode(Generic[KT, VT]):
    def __init__(
        self,
        key: KT,
        value: Optional[VT] = None,
        left: Optional['BinaryTreeNode[KT, VT]'] = None,
        right: Optional['BinaryTreeNode[KT, VT]'] = None,
    ):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


    def __repr__(self):
        return str({
            'key': self.key,
            'value': self.value,
            'address': hex(id(self)),
            'has_left': bool(self.left),
            'has_right': bool(self.right),
        })
