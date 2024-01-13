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


def generate_linked_list(values: list) -> LinkedList:
    return LinkedList().add_all(values)


GET_BY_INDEX_PARAMS = [(2, 3), (0, 1), (5, 6)]


@pytest.mark.parametrize("index, expected_result", GET_BY_INDEX_PARAMS)
def test_get_by_index(linked_list_with_values, index, expected_result):

    result = linked_list_with_values.get_by_index(index).get_value()

    assert expected_result == result


def test_get_by_index_value_error():
    pass


GET_BY_VALUE_PARAMS = [(4, 4), (6, 6), (7, None), (-1, None), ('A', None)]


@pytest.mark.parametrize("value, expected_result", GET_BY_VALUE_PARAMS)
def test_get_by_value(linked_list_with_values, value, expected_result):
    found_node = linked_list_with_values.get_by_value(value)
    try:
        result = found_node.get_value()
    except AttributeError:
        result = found_node

    assert expected_result == result


INDEX_OF_PARAMS = [(5, 4), (1, 0), (6, 5), (7, None), (-1, None)]


@pytest.mark.parametrize("value, expected_result", INDEX_OF_PARAMS)
def test_index_of(linked_list_with_values, value, expected_result):

    result = linked_list_with_values.index_of(value)

    assert result == expected_result


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


REMOVE_BY_VALUE_PARAMS = [(2, 2), (17, None), (1, 1), (6, 6)]

@pytest.mark.parametrize("value, expected_value", REMOVE_BY_VALUE_PARAMS)
def test_remove_by_value(linked_list_with_values, value, expected_value):

    expected_return_result = expected_value
    removed_node = linked_list_with_values.remove_by_value(value)

    try:
        return_result = removed_node.get_value()
    except:
        return_result = removed_node

    expected_result = None
    result = linked_list_with_values.get_by_value(value)

    assert expected_return_result == return_result
    assert expected_result == result


REMOVE_BY_INDEX_PARAMS = [(1, 2), (2, 3), (5, 6)]


@pytest.mark.parametrize("index, value", REMOVE_BY_INDEX_PARAMS)
def test_remove_by_index(linked_list_with_values, index, value):

    expected_return_result = value
    removed_node = linked_list_with_values.remove_by_index(index)

    try:
        return_result = removed_node.get_value()
    except:
        return_result = removed_node

    expected_result = None
    result = linked_list_with_values.get_by_value(value)

    

    assert expected_return_result == return_result
    assert expected_result == result


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


INSERT_PARAMS = [(3, 2), (4, 1), (8, 0)]


@pytest.mark.parametrize("value, index", INSERT_PARAMS)
def test_insert(linked_list_with_values, value, index):

    linked_list_with_values.insert(index, value)

    expected_result = value
    result = linked_list_with_values.get_by_index(index).get_value()

    assert result == expected_result


def test_length_adding(linked_list_empty):
    linked_list_empty.add_to_head(1)
    linked_list_empty.add_to_tail(2)
    linked_list_empty.add_to_head(1)
    linked_list_empty.add_to_tail(2)
    linked_list_empty.insert(1, 5)

    expected_result = 5
    result = linked_list_empty.length

    assert result == expected_result


def test_length_removing(linked_list_with_values):
    linked_list_with_values.remove_by_index(1)
    linked_list_with_values.remove_by_value(6)
    linked_list_with_values.remove_head()
    linked_list_with_values.remove_tail()

    expected_result = 2
    result = linked_list_with_values.length

    assert result == expected_result


ADD_ALL_PARAMS = [([1, 2, 3, 4, 5, 6]), ([1, 2, 3]), ([1])]


@pytest.mark.parametrize("values", ADD_ALL_PARAMS)
def test_add_all(linked_list_empty, values):
    expected_length = len(values)

    linked_list_empty.add_all(values)

    expected_result = expected_length
    result = linked_list_empty.length

    assert expected_result == result


def test_sort():

    expected_result = LinkedList().add_all([1, 2, 3, 4, 5, 6])
    linked_list_unsorted = LinkedList().add_all([6, 2, 5, 3, 4, 1])

    result = linked_list_unsorted.sort()

    assert result == expected_result


@pytest.mark.parametrize("index", [(-1), (15), ('A'), ('0')])
def test_get_index_raises_ValueError(linked_list_with_values, index):
    with pytest.raises(ValueError):
        linked_list_with_values.get_by_index(index)


@pytest.mark.parametrize("index", [(-1), (15), ('A'), ('0')])
def test_insert_raises_ValueError(linked_list_with_values, index):
    value = 1
    with pytest.raises(ValueError):
        linked_list_with_values.insert(index, value)


@pytest.mark.parametrize("index", [(-1), (15), ('A'), ('0')])
def test_remove_by_index_raises_ValueError(linked_list_with_values, index):
    with pytest.raises(ValueError):
        linked_list_with_values.remove_by_index(index)
