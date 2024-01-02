from .node import Node
from typing import Any

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._length = 0

    def add_to_head(self, value: Any) -> None:
        # Add to head of list
        new_node = Node(value=value)
        current_head = self.head

        if current_head:
            new_node.set_next_node(current_head)
            current_head.set_prev_node(new_node)

        if self.tail is None:
            self.tail = current_head

        self.head = new_node
        self._length += 1

    def add_to_tail(self, value: Any) -> None:
        new_node = Node(value=value)
        current_tail = self.tail

        if current_tail:
            new_node.set_prev_node(current_tail)
            current_tail.set_next_node(new_node)

        if self.head is None:
            self.head = new_node

        self.tail = new_node
        self._length += 1


    def add_all(self, values: list)-> None:
        pass


    def insert(self, value: Any) -> None:
        # Add to index
        pass

    def remove(self, value: Any) -> Node:
        # TODO: Remove from head of list
        # TODO: Remove from tail of list
        # TODO: Remove from middle of list
        pass

    def remove_head() -> Node:
        pass

    def remove_tail() -> Node:
        pass

    def get_by_index(self, index: Any) -> Node:
        # TODO: Traverse list
        # TODO: Find element (index)
        # TODO: Return element
        pass

    def get_by_value(self, value: Any) -> Node:
        # TODO: Traverse list
        # TODO: Find element (value)
        # TODO: Return element
        pass

    def length(self) -> int:
        # TODO: Update to traverse list and count elements. 
        # TODO: Or make the current method more robust.
        return self._length

    def __repr__(self) -> str:
        current_node = self.head
        output = " "

        for _ in range(self.length()):
            if current_node:
                output += f"{current_node.get_value()}, "
                current_node = current_node.get_next_node()

        return f"[{output}]"

