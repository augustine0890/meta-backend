class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    # Time: O(1) and Space: O(1)
    def append(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1
        return self

    # Time: O(1) and Space: O(1)
    def prepend(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._length += 1
        return self

    # Time: O(1) and Space: O(1)
    def pop_left(self):
        if not self._length:
            raise Exception("list is empty")

        removed_value = self.head.value

        if self._length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self._length -= 1
        return removed_value


my_list = SinglyLinkedList()
print(my_list._length)
print(my_list.append(2))
print("Length", my_list._length)
print("Head", my_list.head.value)
print("Tail", my_list.tail.value)
my_list.prepend(11)
print("Head after prepend", my_list.head.value)
