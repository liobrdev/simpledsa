from typing import Generic, Optional, TypeVar


DT = TypeVar('DT')
KT = TypeVar('KT')
VT = TypeVar('VT')


class LinearNode(Generic[DT]):
    def __init__(self, data: DT):
        self.data = data
        self.next: Optional['LinearNode[DT]'] = None

    def __repr__(self):
        return str({
            'data': self.data,
            'address': hex(id(self)),
            'has_next': bool(self.next)
        })


class BinaryTreeNode(Generic[KT, VT]):
    def __init__(self, key: KT, value: Optional[VT] = None):
        self.key = key
        self.value = value
        self.left: Optional['BinaryTreeNode[KT, VT]'] = None
        self.right: Optional['BinaryTreeNode[KT, VT]'] = None


    def __repr__(self):
        return str({
            'key': self.key,
            'value': self.value,
            'address': hex(id(self)),
            'has_left': bool(self.left),
            'has_right': bool(self.right),
        })


class AVLTreeNode(BinaryTreeNode[KT, VT]):
    def __init__(self, key: KT, value: Optional[VT] = None):
        self.key = key
        self.value = value
        self.left: Optional['AVLTreeNode[KT, VT]'] = None
        self.right: Optional['AVLTreeNode[KT, VT]'] = None
        self.height: int = 0
