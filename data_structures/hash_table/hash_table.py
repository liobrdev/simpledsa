from dataclasses import dataclass
from typing import Generic, List, Literal, Optional, Tuple, Type, TypeVar

from ..utils import next_prime


VT = TypeVar('VT')

@dataclass
class HashTable(Generic[VT]):
    def __init__(self, **kwargs: VT):
        if not kwargs:
            self._data_type = None
        else:
            self._data_type = self._check_data_types(**kwargs)

        self._array: List[Tuple[str, VT] | None | Tuple[()]] = \
            [None] * max(next_prime(len(kwargs) * 2), 5)
        
        for key, value in kwargs.items():
            self._insert_item(key, value)


    def _check_data_types(self, **kwargs: VT) -> Type[VT]:
        kwargs_values = list(kwargs.values())

        for index, value in enumerate(kwargs_values):
            if not isinstance(value, type(kwargs_values[index - 1])):
                raise TypeError('All entries must have the same type!')
        
        return type(kwargs_values[0])


    def _check_load(self) -> Literal[-1, 0, 1]:
        num_entries = len([entry for entry in self._array if entry])
        num_slots = len(self._array)

        if num_entries / num_slots < 1 / 6:
            return -1

        num_empty = len([entry for entry in self._array if entry is None])

        if num_empty / num_slots < 1 / 3:
            return 1

        return 0


    def _expand_array(self):
        old_array = self._array
        self._array = [None] * max(next_prime(len(self._array) * 2), 13)

        for entry in old_array:
            if entry:
                self._insert_item(entry[0], entry[1])


    def _shrink_array(self):
        entries = [entry for entry in self._array if entry]
        self._array = [None] * max(next_prime(len(entries) * 2), 5)

        for key, value in entries:
            self._insert_item(key, value)


    def _hash_key(self, key: str, retry: int) -> int:
        if not key or not isinstance(key, str):
            raise TypeError('Key must be a non-empty string!')

        return hash(key + key[-retry:] * retry * int(2 ** (retry / 2))) % \
            len(self._array)


    def _search_array(self, key: str) -> Tuple[int, Optional[Tuple[str, VT]]]:
        retry: int = 0

        while retry < 25:
            index = self._hash_key(key, retry)

            try:
                entry = self._array[index]
            except IndexError:
                raise IndexError(
                    f'Hash function returned index ({index})'
                    f' outside of range(0, {len(self._array)})!')

            if entry is None or (entry and entry[0] == key):
                return (index, entry)

            retry += 1

        raise RuntimeError(
            f"Could not find key '{key}' after {retry} tries!")


    def _insert_item(self, key: str, value: VT, will_resize: bool = False):
        if not key or not isinstance(key, str):
            raise TypeError('Key must be a non-empty string!')

        if not self._data_type:
            self._data_type = type(value)
        elif not isinstance(value, self._data_type):
            raise TypeError(f"Value must be of type {self._data_type}!")

        index, entry = self._search_array(key)

        if entry is None:
            self._array[index] = (key, value)

            if will_resize:
                resize = self._check_load()

                if resize == 1:
                    return self._expand_array()
                elif resize == -1:
                    return self._shrink_array()
        else:
            raise ValueError(f"Key '{key}' already exists!")


    def __getitem__(self, key: str) -> VT:
        if not key or not isinstance(key, str):
            raise TypeError('Key must be a non-empty string!')

        entry = self._search_array(key)[1]

        if entry:
            return entry[1]
        else:
            raise KeyError(f"Key '{key}' not found!")


    def __setitem__(self, key: str, value: VT):
        if not key or not isinstance(key, str):
            raise TypeError('Key must be a non-empty string!')

        if self._data_type and not isinstance(value, self._data_type):
            raise TypeError(f"Value must be of type {self._data_type}!")

        index, entry = self._search_array(key)

        if entry:
            self._array[index] = (key, value)
        else:
            raise KeyError(f"Key '{key}' not found!")


    def __delitem__(self, key: str):
        if not key or not isinstance(key, str):
            raise TypeError('Key must be a non-empty string!')

        index, entry = self._search_array(key)

        if entry:
            self._array[index] = ()
        else:
            raise KeyError(f"Key '{key}' not found!")


    def __len__(self) -> int:
        return len([entry for entry in self._array if entry])


    def __repr__(self) -> str:
        return str({ entry[0]: entry[1] for entry in self._array if entry })


    def get(self, key: str) -> VT:
        return self.__getitem__(key)


    def put(self, key: str, value: VT):
        self._insert_item(key, value, True)


    def update(self, key: str, value: VT):
        return self.__setitem__(key, value)


    def delete(self, key: str):
        return self.__delitem__(key)

