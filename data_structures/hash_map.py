from typing import Any


class HashMap:
    
    def __init__(self, size:int) -> None:
        self.array_size = size
        self.array = [None for _ in range(self.array_size)]

    def _hash(self, key: Any) -> int:
        return sum(key.encode())

    def _compress(self, hash_code: int) -> int:
        return hash_code % self.array_size

    def assign(self):
        pass

    def retrieve(self):
        pass


hash_map = HashMap(5)
my_hash = hash_map._hash("Stuff")

print(type(hash_map._compress(my_hash)))