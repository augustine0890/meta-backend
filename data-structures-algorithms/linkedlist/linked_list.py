class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    # Add your insert_beginning and stringify_list methods below:
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            string_list += str(current_node.get_value())
            if current_node.get_next_node() is not None:
                string_list += " --> "
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.head_node
        previous_node = None
        while current_node:
            if current_node.get_value() == value_to_remove:
                if previous_node:
                    previous_node.set_next_node(current_node.get_next_node())
                else:
                    self.head_node = current_node.get_next_node()
                return
            previous_node, current_node = current_node, current_node.get_next_node()

    def swap(self, val1, val2):
        if val1 == val2:
            print("Elements are the same - no swap needed")
            return

        node1 = self.head_node
        node2 = self.head_node
        node1_prev = None
        node2_prev = None

        # Find nodes with val1 and val2
        while node1 and node1.get_value() != val1:
            node1_prev = node1
            node1 = node1.get_next_node()

        while node2 and node2.get_value() != val2:
            node2_prev = node2
            node2 = node2.get_next_node()

        # Check if both elements are in the list
        if not node1 or not node2:
            print("Swap not possible - one or more element is not in the list")
            return

        # Swapping the head node if needed
        if node1_prev is None:
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        # Swapping the next nodes of node1 and node2
        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)

    def nth_last_node(self, n):
        nth_node = None
        tail_pointer = self.head_node
        count = 1
        while tail_pointer != None:
            tail_pointer = tail_pointer.get_next_node()
            count += 1
            if count >= n + 1:
                if nth_node == None:
                    nth_node = self.head_node
                else:
                    nth_node = nth_node.get_next_node()
        return nth_node


ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())
print(ll.nth_last_node(2).get_value())

ll = LinkedList()
for i in range(10):
    ll.insert_beginning(i)

print(ll.stringify_list())
ll.swap(9, 8)
print(ll.stringify_list())
