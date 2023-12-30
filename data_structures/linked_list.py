from node import Node

class LinkedList:
    def __init__(self, value, next_node=None):
        self.head = Node(value=value, next_node=next_node)
        self._length = 1

    def add(self, value):
        new_node = Node(value=value, next_node=self.head)
        self.head = new_node
        self._length += 1

    def remove(self):
        pass

    def get(self):
        pass

    def length(self):
        return self._length

    def __repr__(self):
        current_node = self.head
        output = " "

        for _ in range(self.length()):
            if current_node:
                output += f"{current_node.get_value()}, "
                current_node = current_node.get_next_node()

        return f"[{output}]"

if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    my_linked_list.add(2)
    my_linked_list.add(3)
    my_linked_list.add(4)

    print(my_linked_list)