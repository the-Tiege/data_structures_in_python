class Node:
    """
    A Node for building linked data structures

    Args:
        value: The value held by the Node.
        next_node (Node, optional): The next Node in the linked structure.
        prev_node (Node, optional): The previous Node in the linked structure.

    Attributes:
        value: The value held by the node.
        next_node (Node): The next node in the linked structure.
        prev_node (Node): The previous node in the linked structure.
    """

    def __init__(self, value, next_node=None, prev_node=None):
        """
        Initialise a new Node.

        Args:
            value: The value held by the node.
            next_node (Node, optional): The next Node in the linked structure.
            prev_node (Node, optional): The previous Node in the linked structure.
        """
        self.value = value
        self.next_node = next_node
        self.prev_node


    def set_next_node(self, next_node):
        """
        Set the next NOde in the linked structure.

        Args:
            next_node (Node, optional): The next Node in the linked structure.
        """
        self.next_node = next_node

    def get_next_node(self):
        """
        Get the next Node in the linked structure.

        Returns:
            next_node (Node): The next Node in the linked structure.
        """
        return self.next_node
    
    def set_prev_node(self, prev_node):
        """
        Set the previous NOde in the linked structure.

        Args:
            prev_node (Node, optional): The previous Node in the linked structure.
        """
        self.prev_node = prev_node

    def get_prev_node(self):
        """
        Get the previous Node in the linked structure.

        Returns:
            prev_node (Node): The previous Node in the linked structure.
        """
        return self.prev_node
    
    def get_value(self):
        """
        Get the value held by the Node.

        Returns:
            value: The value held by the node.
        """
        return self.value
    
    def set_value(self, value):
        """
        Sets the value held by thr Node.

        Args:
            Any: the value held by the Node.
        """
        self.value = value

    def __str__(self):
        return f"Node({self.value})"
    

if __name__ == '__main__':
    node_1 = Node(1)

    print(node_1)