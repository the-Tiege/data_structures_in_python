from typing import Any
from node import Node
from linked_list import LinkedList


class HashMap:
    
    def __init__(self, size:int) -> None:
        self.array_size = size
        self.array = [LinkedList() for _ in range(self.array_size)]

    def _hash(self, key: Any) -> int:
        return sum(key.encode())

    def _compress(self, hash_code: int) -> int:
        return hash_code % self.array_size

    def assign(self, key: Any, value: Any) -> None:
        hash_code = self._hash(key)
        array_index = self._compress(hash_code)
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        for item in list_at_array:
            if item[0] == key:
                item[1] = value

        self.array[array_index] = [key, value]


    def retrieve(self, key: Any) -> Any:
        hash_code = self._hash(key)
        array_index = self._compress(hash_code)

        payload = self.array[array_index]

        if payload[0] is None or payload[0] is not key:
            return None
        else:
            return payload[1]


