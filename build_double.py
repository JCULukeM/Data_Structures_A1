from double_linked_list import DoubleLinkedList, ListNode



node1 = ListNode(15, 1)
node2 = ListNode(8, 2)
node3 = ListNode("Yeet", 3)
node4 = ListNode(18, 4)

track = DoubleLinkedList()
print("track length: %i" % track.list_length())

for current_node in [node1, node2, node3, node4]:
    track.add_list_item(current_node)
    print("track length %i" % track.list_length())
    track.output_list()

results = track.unordered_search(15)
print(results)

track.output_list()
print("index 3 is {}".format(track[3]))
