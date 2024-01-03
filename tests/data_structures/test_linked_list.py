from data_structures.linked_list import LinkedList
import pytest


@pytest.fixture
def linked_list_with_values():
    linked_list = LinkedList()

    linked_list.add_to_tail(1)
    linked_list.add_to_tail(2)
    linked_list.add_to_tail(3)
    linked_list.add_to_tail(4)
    linked_list.add_to_tail(5)
    linked_list.add_to_tail(6)

    return linked_list


@pytest.fixture
def linked_list_empty():
    return LinkedList()


def test_get_by_index(linked_list_with_values):
    index = 2

    expected_result = 3
    result = linked_list_with_values.get_by_index(index).get_value()

    assert expected_result == result


def test_get_by_value(linked_list_with_values):
    value = 4

    expected_result = 4
    result = linked_list_with_values.get_by_value(value).get_value()

    assert expected_result == result


def test_index_of(linked_list_with_values):
    value = 5

    expected_result = 4
    result = linked_list_with_values.index_of(value)

    assert result == expected_result


def test_remove_by_value(linked_list_with_values):
    linked_list_with_values.remove_by_value(2)

    expected_result = None
    result = linked_list_with_values.get_by_value(2)

    assert expected_result == result


def test_remove_tail(linked_list_with_values):
    old_tail = linked_list_with_values.remove_tail()

    expected_result_old_tail = 6
    result_old_tail = old_tail.get_value()

    expected_result_new_tail = 5
    result_new_tail = linked_list_with_values.tail.get_value()

    assert expected_result_old_tail == result_old_tail
    assert expected_result_new_tail == result_new_tail


def test_remove_head(linked_list_with_values):
    old_head = linked_list_with_values.remove_head()

    expected_result_old_head = 1
    result_old_head = old_head.get_value()

    expected_result_new_head = 2
    result_new_head = linked_list_with_values.head.get_value()

    assert expected_result_old_head == result_old_head
    assert expected_result_new_head == result_new_head


def test_add_to_head(linked_list_empty):
    value = 5
    linked_list_empty.add_to_head(value)

    result = linked_list_empty.head.get_value()
    expected_result = value

    assert result == expected_result


def test_add_to_tail(linked_list_empty):
    value = 5
    linked_list_empty.add_to_tail(value)

    result = linked_list_empty.tail.get_value()
    expected_result = value

    assert result == expected_result


def test_insert(linked_list_with_values):
    value = 3
    index = 2

    linked_list_with_values.insert(value, index)

    expected_result = value
    result = linked_list_with_values.get_by_index(index).get_value()

    assert result == expected_result


def test_length():
    pass

def test_add_all():
    pass
