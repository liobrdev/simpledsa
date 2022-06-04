from typing import Generic, Optional, TypeVar


DT = TypeVar('DT')

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


class BinaryTreeNode(Generic[DT]):
    def __init__(self, data: DT):
        self.data = data
        self.left: Optional['BinaryTreeNode[DT]'] = None
        self.right: Optional['BinaryTreeNode[DT]'] = None

    def __repr__(self):
        return str({
            'data': self.data,
            'address': hex(id(self)),
            'has_left': bool(self.left),
            'has_right': bool(self.right),
        })        

