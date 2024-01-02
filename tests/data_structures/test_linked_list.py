from data_structures.linked_list import LinkedList
import pytest

@pytest.fixture
def linked_list_with_values():
    linked_list = LinkedList()

    linked_list.add_to_head(1)
    linked_list.add_to_head(2)
    linked_list.add_to_head(3)
    linked_list.add_to_head(4)
    linked_list.add_to_head(5)
    linked_list.add_to_head(6)

    return linked_list

@pytest.fixture
def linked_list_empty():
    return LinkedList()


def test_get_by_index(linked_list_with_values):
    pass

def test_get_by_value(linked_list_with_values):
    pass

def test_index_of(linked_list_with_values):
    pass
    

def test_remove_by_value(linked_list_with_values):
    linked_list_with_values.remove_by_value(2)

    expected_result = None
    result = linked_list_with_values.get_by_value(2)

    assert expected_result == result

def test_remove_tail(linked_list_with_values):
    old_tail = linked_list_with_values.remove_tail()

    expected_result = 1
    result = old_tail.get_value()

    assert expected_result == result

def test_remove_head(linked_list_with_values):
    old_head = linked_list_with_values.remove_head()

    expected_result_old_head = 6
    result_old_head = old_head.get_value()

    expected_result_new_head = 5
    result_new_head = linked_list_with_values.head.get_value()

    assert expected_result_old_head == result_old_head
    assert expected_result_new_head == result_new_head


def test_add_to_head(linked_list_empty):
    linked_list_empty.add_to_head(5)

    result = linked_list_empty.head.get_value()
    expected_result = 5

    assert result == expected_result


def test_add_to_tail(linked_list_empty):
    linked_list_empty.add_to_tail(5)

    result = linked_list_empty.tail.get_value()
    expected_result = 5

    assert result == expected_result

def test_insert(linked_list_with_values):
    value = 3
    index = 2

    linked_list_with_values.insert(value, index)

    expected_result = value
    result = linked_list_with_values.get_by_index(index).get_value()

    assert result == expected_result

