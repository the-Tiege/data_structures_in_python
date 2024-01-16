from data_structures import linked_list, node


expected_result = linked_list.LinkedList()
expected_result.add_all([1, 2, 3, 4, 5, 6])
linked_list_unsorted = linked_list.LinkedList()
linked_list_unsorted.add_all([6, 2, 5, 3, 4, 1])



linked_list_unsorted.insert(5,7)

linked_list_unsorted.sort()

print(linked_list_unsorted)
