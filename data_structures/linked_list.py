"""
Linked List

Data structure containing an ordered set of data elements (nodes).
Each node contains a link to the next node in the list and the previous node.

Classes:
- LinkedList: A class containing the methods required for a linked list datastructure.

"""

from typing import Any

from .node import Node


class LinkedList:
    """
    A doubly linked list implementation.

    Attributes:
    - _head: Node
             The head node indicates the start of the linked list.
    - _tail: Node
             The tail node indicates the end of the linked list.
    - _length: int
             int value representing the current number of nodes in the list.  

    Methods:

        - __init__: Initializes the linked list.
        - length (property): Returns the length of the linked list.
        - head (property): Returns the head node of the linked list.
        - tail (property): Returns the tail node of the linked list.
        - add_to_head: Adds a node to the head of the linked list.
        - add_to_tail: Adds a node to the tail of the linked list.
        - add_all: Appends a list of values to the tail of the linked list.
        - insert: Inserts a node at the specified index.
        - remove_by_value: Removes the first occurrence of a node with the specified value.
        - remove_by_index: Removes the node at the specified index.
        - remove_head: Removes the head node.
        - remove_tail: Removes the tail node.
        - get_by_index: Retrieves a node at the specified index.
        - get_by_value: Searches for a node with the specified value and returns the first occurrence.
        - index_of: Returns the index of the first occurrence of a node with the specified value.
        - __repr__: Returns a string representation of the linked list.
        - _remove_node: Helper method to remove a specified node from the linked list.
        - sort: Sorts the linked list in ascending order.

    """

    def __init__(self) -> None:
        """
        Initialise LinkedList 
        """
        self._head = None
        self._tail = None
        self._length = 0

    @property
    def length(self) -> int:
        """
        Returns LinkedList length

       Returns:
       Type: int
             The length of the LinkedList
        """
        return self._length

    @length.setter
    def length(self, value) -> None:
        """
        Function added to make length editable.
        Doesn't allow _length to be altered this way.
        """

    @property
    def head(self) -> Node:
        """
        Returns the head of the LinkedList

       Returns:
       Node: The first node in the list.
        """
        return self._head

    @head.setter
    def head(self, value: Any) -> None:
        """
        Calls add_to_head method to properly add
        the head node to the list.

        Parameters:
        - value: Any
                 The value stored in the Node
        """
        self.add_to_head(value)

    @property
    def tail(self) -> Node:
        """
        Returns the tail node.
        The last node in the list

        Returns:
        Node: The tail node.
        """
        return self._tail

    @tail.setter
    def tail(self, value: Any) -> None:
        """
        Calls the add_to_tail method to 
        add tail node to the list.

        Parameters:
        - value: Any
                 The value stored in the node.
        """
        self.add_to_tail(value)

    def add_to_head(self, value: Any) -> None:
        """
        Creates a Node containig he value passed 
        as a parameter and appends it to the head 
        of the LinkedList

        Parameters:
        - value: Any
                 The value to be stored in the node.
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
        Creates a node containing the value passed 
        as a parameter and appends it to the end of the 
        LinkedList.

        Parameters:
        - value: Any
                 The value to be contained in the node.
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
        Appends a list of values to the tail 
        f the LinkedList using the add_to_tail 
        method.

        Parameters:
        - values: list
                  List of values to be added to the LinkedList as nodes.
        """

        for value in values:
            self.add_to_tail(value)

    def insert(self, index: int, value: Any) -> None:
        """
        Creates a node containing the entered value
        and inserts it at the required index.

        Parameters:
        - index: int
                 The index to insert the node at.
        - value: Any
                 The value contained in the node.
        """

        if not isinstance(index, int):
            raise ValueError("Index must be of type int")

        if index < 0 or index > self.length:
            raise IndexError("Index outside of range")

        if index == 0:
            self.add_to_head(value)

        elif index == self._length:
            self.add_to_tail(value)

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
        Searches the LinkedList for the entered value 
        and removes its first occurrence.

        Parameters:
        - value: Any
                 The value of the node to be removed.
        Returns:
        Node: The node containing the value to be removed.
        """
        node_to_remove = self.get_by_value(value)

        if node_to_remove == self._tail:
            self.remove_tail()

        elif node_to_remove == self._head:
            self.remove_head()

        elif node_to_remove:
            node_before = node_to_remove.get_prev_node()
            node_after = node_to_remove.get_next_node()
            node_before.set_next_node(node_after)
            node_after.set_prev_node(node_before)
            self._length -= 1

        return node_to_remove

    def remove_by_index(self, index: int) -> Node:
        """
        Reoves the node at the specified index.

        Parameters:
        - index: int
                 The index of the Node to be removed.
        Returns:
        Node: The Node to be removed.

        Raises: ValueError if index is not an int, is less 
        than zero or is greater than the length of the list.
        """

        if not isinstance(index, int) or index < 0 or index > self.length:
            raise ValueError

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
        Removes the head node

       Returns:
       Node: The old head node.

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
        Removes the tail Node.

        Returns:
        Node: The old tail node.
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

    def get_by_index(self, index: int) -> Node:
        """
        Retrieves a node at the specified index 

        Parameters:
        - index: int
                 The index of the node to be retrieved. 
       Returns:
       Node: The node at the entered index.
        """
        if not isinstance(index, int) or index < 0 or index > self.length:
            raise ValueError

        if index == 0:
            return self._head

        if index == self._length - 1:
            return self._tail

        current_node = self._head
        current_index = 0

        while current_node and current_index < index:
            current_node = current_node.get_next_node()
            current_index += 1

        return current_node

    def get_by_value(self, value: Any) -> Node:
        """
        Searches the LinkedList for a node containing
        the specified value. Returns the first node 
        containing this value.

        Parameters:
        - value: Any
                 The value of the node to find.
       Returns:
       Node: The first Node containing the specified value.
        """
        current_node = self._head
        search_node = None
        node_in_list = False

        while current_node:
            if current_node.get_value() == value:
                search_node = current_node
                node_in_list = True
                break
            current_node = current_node.get_next_node()

        if node_in_list:
            return search_node

        return None

    def index_of(self, value: Any) -> int:
        """
        Returns the index of the first occurrence 
        of the specified value

        Parameters:
        - value: Any
                 The value of the Node to be found.
        Returns:
        Node: The first occurrence of a node containing the specified value.
        """
        current_node = self._head
        index = 0
        found_value = False

        while current_node:
            if current_node.get_value() == value:
                found_value = True
                break
            current_node = current_node.get_next_node()
            index += 1

        if found_value:
            return index

        return None

    def __repr__(self) -> str:
        """
        Returns a string representation of the
        linked_list

       Returns:
       str: String representation of the LinkedList.
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

    def _remove_node(self, node_to_remove: Node) -> Node:
        """
        Internal method used to remove a node from the list

        Parameters:
        - node_to_remove: Node
                    description
        Returns:
        Node: The removed node
        """

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

    def sort(self) -> None:
        """
        Sorts the list in ascending order using selection sort.
        The method iterates over unsorted portion the list and finds the min value.
        Once found it removes this value and inserts it in the left most position
        this element is then considered sorted. The process continues until
        the list is sorted.
        """

        for i in range(self.length - 1):
            min_node = self.get_by_index(i)
            current_node = self.get_by_index(i)

            while current_node:
                if current_node.get_value() < min_node.get_value():
                    min_node = current_node
                current_node = current_node.get_next_node()

            min_node = self._remove_node(min_node)
            self.insert(i, min_node.get_value())
