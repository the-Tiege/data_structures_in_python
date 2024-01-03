from .node import Node
from typing import Any


class LinkedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._length = 0

    @property
    def length(self) -> int:
        # TODO: Update to traverse list and count elements.
        # TODO: Or make the current method more robust.
        return self._length

    @length.setter
    def length(self, value) -> None:
        # TODO: Update to traverse list and count elements.
        # TODO: Or make the current method more robust.
        self._length = value

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self.add_to_head(value)

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value):
        self.add_to_tail(value)

    def add_to_head(self, value: Any) -> None:
        # Add to head of list
        new_node = Node(value=value)
        current_head = self._head

        if current_head:
            new_node.set_next_node(current_head)
            current_head.set_prev_node(new_node)

        if self._tail is None:
            self._tail = current_head

        self._head = new_node
        self._length += 1

    def add_to_tail(self, value: Any) -> None:
        new_node = Node(value=value)
        current_tail = self._tail

        if current_tail:
            new_node.set_prev_node(current_tail)
            current_tail.set_next_node(new_node)

        if self._head is None:
            self._head = new_node

        self._tail = new_node
        self._length += 1

    def add_all(self, values: list) -> None:
        pass

    def insert(self, value: Any) -> None:
        # Add to index
        pass

    def remove_by_value(self, value: Any) -> Node:
        # TODO: Remove from head of list
        # TODO: Remove from tail of list
        # TODO: Remove from middle of list
        pass

    def remove_by_index(self, value: Any) -> Node:
        # TODO: Remove from head of list
        # TODO: Remove from tail of list
        # TODO: Remove from middle of list
        pass

    def remove_head(self) -> Node:
        current_head = self._head
        new_head = None

        if current_head:
            new_head = current_head.get_next_node()
            new_head.set_prev_node(None)
            self._head = new_head
            self._length -= 1

        if current_head == self._tail and self._length == 1:
            self.remove_tail()

        return current_head

    def remove_tail(self) -> Node:
        current_tail = self._tail
        new_tail = None

        if current_tail:
            new_tail = current_tail.get_prev_node()
            new_tail.set_next_node(None)
            self._tail = new_tail
            self._length -= 1

        if current_tail == self._head and self._length == 1:
            self.remove_head()

        return current_tail

    def get_by_index(self, index: Any) -> Node:
        if index >= self._length:
            raise IndexError
        elif index == 0:
            return self._head
        elif index == self._length - 1:
            return self._tail

        current_node = self._head
        current_index = 0

        while current_node and current_index < index:
            current_node = current_node.get_next_node()
            current_index += 1

        return current_node

    def get_by_value(self, value: Any) -> Node:
        current_node = self._head
        search_node = None

        while current_node:
            if current_node.get_value() == value:
                search_node = current_node
                break
            current_node = current_node.get_next_node()
        return search_node
    
    def index_of(self, value):
        current_node = self._head
        index = 0

        while current_node:
            if current_node.get_value() == value:
                break
            current_node = current_node.get_next_node()
            index += 1
        return index


    def __repr__(self) -> str:
        current_node = self.head
        output = " "

        for _ in range(self.length):
            if current_node:
                output += f"{current_node.get_value()}"
                if current_node.get_next_node():
                    output += ","
                output += " "
                current_node = current_node.get_next_node()

        return f"[{output}]"
