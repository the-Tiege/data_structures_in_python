from data_structures.node import Node

def test_node_creation():
    value = 42
    node = Node(value)

    assert node.get_value() == value
    assert node.get_next_node() is None
    assert node.get_prev_node() is None

def test_set_next_node():
    node_1 = Node(1)
    node_2 = Node(2)

    node_1.set_next_node(node_2)

    assert node_1.get_next_node() == node_2

def test_set_prev_node():
    node_1 = Node(1)
    node_2 = Node(2)

    node_2.set_prev_node(node_1)

    assert node_2.get_prev_node() == node_1

def test_set_value():
    node = Node(1)
    new_value = 42

    node.set_value(new_value)

    assert node.get_value() == new_value

def test_node_str_repr():
    value = 42
    node = Node(value)

    assert str(node) == f"Node({value})"