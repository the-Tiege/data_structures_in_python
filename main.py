from data_structures import linked_list, node


expected_result = linked_list.LinkedList()
expected_result.add_all([6, 5, 4, 3, 2, 1, 0, -1])
linked_list_unsorted = linked_list.LinkedList()
linked_list_unsorted.add_all([6, 100, 50, 2, 99, -1])


linked_list_unsorted.sort()
expected_result.sort()

print(linked_list_unsorted)
print(expected_result)
