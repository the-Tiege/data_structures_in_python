from data_structures import linked_list, node

new_list = linked_list.LinkedList()
new_list.add_to_head(1)
new_list.add_to_head(2)
new_list.add_to_head(3)
new_list.add_to_head(4)
new_list.add_to_head(5)
new_list.add_to_head(6)

old_head = new_list.remove_tail()

print(old_head)
print(new_list.tail)


print(new_list)