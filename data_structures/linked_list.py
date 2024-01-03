"""
NAME

Description

Classes:
- classes.

Example Usage:
Create instances

implement methods

Note: if required
"""

from .node import Node
from typing import Any


class LinkedList:
    """
    Description

    Attributes:


    Methods:

    """

    def __init__(self) -> None:
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
        self._head = None
        self._tail = None
        self._length = 0

    @property
    def length(self) -> int:
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
        # TODO: Update to traverse list and count elements.
        # TODO: Or make the current method more robust.
        return self._length

    @length.setter
    def length(self, value) -> None:
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
        # TODO: Update to traverse list and count elements.
        # TODO: Or make the current method more robust.
        pass

    @property
    def head(self):
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
        return self._head

    @head.setter
    def head(self, value):
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
        self.add_to_head(value)

    @property
    def tail(self):
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
        return self._tail

    @tail.setter
    def tail(self, value):
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
        self.add_to_tail(value)

    def add_to_head(self, value: Any) -> None:
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
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
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
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
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """

        for value in values:
            self.add_to_tail(value)

    def insert(self, index: int, value: Any) -> None:
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """

        if index >= self.length:
            raise IndexError

        if index == 0:
            self.add_to_head(value)

        elif index == self._length - 1:
            self.add_to_tail

        else:
            node_to_insert = Node(value)
            node_after = self.get_by_index(index)
            node_before = node_after.get_prev_node()
            node_to_insert.set_next_node(node_after)
            node_to_insert.set_prev_node(node_before)
            node_before.set_next_node(node_to_insert)
            node_after.set_prev_node(node_to_insert)
            self._length += 1

    def remove_by_value(self, value: Any) -> Node:
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
        node_to_remove = self.get_by_value(value)

        if node_to_remove == self._tail:
            self.remove_tail()

        elif node_to_remove == self._head:
            self.remove_head()

        else:
            node_before = node_to_remove.get_prev_node()
            node_after = node_to_remove.get_next_node()
            node_before.set_next_node(node_after)
            node_after.set_prev_node(node_before)
            self._length -= 1

        return node_to_remove

    def remove_by_index(self, index: int) -> Node:
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
        node_to_remove = self.get_by_index(index)

        if node_to_remove == self._tail:
            self.remove_tail()

        elif node_to_remove == self._head:
            self.remove_head()

        else:
            node_before = node_to_remove.get_prev_node()
            node_after = node_to_remove.get_next_node()
            node_before.set_next_node(node_after)
            node_after.set_prev_node(node_before)
            self._length -= 1

        return node_to_remove

    def remove_head(self) -> Node:
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
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
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
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
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
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
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
        current_node = self._head
        search_node = None

        while current_node:
            if current_node.get_value() == value:
                search_node = current_node
                break
            current_node = current_node.get_next_node()
        return search_node

    def index_of(self, value):
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
        current_node = self._head
        index = 0

        while current_node:
            if current_node.get_value() == value:
                break
            current_node = current_node.get_next_node()
            index += 1
        return index

    def __repr__(self) -> str:
        """
        description

        Parameters:
        - param name: Type
                   description
       Returns:
       Type: description

       Raises:
       Type: description
        """
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
