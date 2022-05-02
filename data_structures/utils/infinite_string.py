from typing import Literal


class InfiniteString(str):
    def __eq__(self, other: object) -> bool:
        if isinstance(other, type(self)):
            return True
        elif isinstance(other, str):
            return False
        else:
            raise TypeError(
                'Unsupported operand type(s) for ==:' +
                f" 'InfiniteString' and '{type(other)}'")


    def __ge__(self, other: object) -> Literal[True]:
        if not isinstance(other, (type(self), str)):
            raise TypeError(
                'Unsupported operand type(s) for >=:' +
                f" 'InfiniteString' and '{type(other)}'")

        return True


    def __gt__(self, other: object) -> bool:
        if isinstance(other, type(self)):
            return False
        elif isinstance(other, str):
            return True
        else:
            raise TypeError(
                'Unsupported operand type(s) for >:' +
                f" 'InfiniteString' and '{type(other)}'")


    def __le__(self, other: object) -> bool:
        if isinstance(other, type(self)):
            return True
        elif isinstance(other, str):
            return False
        else:
            raise TypeError(
                'Unsupported operand type(s) for <=:' +
                f" 'InfiniteString' and '{type(other)}'")


    def __lt__(self, other: object) -> Literal[False]:
        if not isinstance(other, (type(self), str)):
            raise TypeError(
                'Unsupported operand type(s) for <:' +
                f" 'InfiniteString' and '{type(other)}'")

        return False


    def __neg__(self) -> Literal['']:
        return ''
