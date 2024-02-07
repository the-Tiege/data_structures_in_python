from typing import Any


class HashMap:
    
    def __init__(self, size:int) -> None:
        self.array_size = size
        self.array = [None for _ in range(self.array_size)]

    def _hash(self, key: Any) -> int:
        return sum(key.encode())

    def _compress(self, hash_code: int) -> int:
        return hash_code % self.array_size

    def assign(self, key: Any, value: Any) -> None:
        hash_code = self._hash(key)
        array_index = self._compress(hash_code)
        self.array[array_index] = [key, value]


    def retrieve(self, key: Any) -> Any:
        hash_code = self._hash(key)
        array_index = self._compress(hash_code)

        payload = self.array[array_index]

        if payload[0] is None or payload[0] is not key:
            return None
        else:
            return payload[1]


