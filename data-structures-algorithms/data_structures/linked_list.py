class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        pre = temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # Time O(n) and Space O(1)
    def find_middle_node(self):
        if not self.head:
            return None
        slow_pointer = fast_pointer = self.head
        while slow_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer

    # Time O(n) and Space O(1)
    def has_loop(self):
        if not self.head:
            return False
        slow_pointer = fast_pointer = self.head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False


"""
Time O(n) and Space O(1)
- Set two pointers, slow and fast at the head of linked list
- Move the fast pointer k steps forward
- Move both slow and fast pointers forward until the fast pointer reaches the last node
- Return the slow pointer
"""


def find_kth_from_end(ll, k):
    slow = fast = ll.head
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(3)
my_linked_list.append(5)
my_linked_list.append(9)
my_linked_list.append(11)
print("Before")
my_linked_list.print_list()
my_linked_list.pop()
print("After")
my_linked_list.print_list()
my_linked_list.pop()
print("First Pop:", my_linked_list.pop_first())
my_linked_list.append(6)
my_linked_list.append(9)
my_linked_list.append(4)
my_linked_list.print_list()
print("Get value of index 3:", my_linked_list.get(3).value)
print("Set value of index 3:", my_linked_list.set_value(3, 7))
print("Get value of index 3:", my_linked_list.get(3).value)
print("Insert value of index 1")
my_linked_list.insert(1, 1)
my_linked_list.print_list()
print("Remove value of index 1")
my_linked_list.remove(1)
my_linked_list.print_list()
print("Reverse")
my_linked_list.reverse()
my_linked_list.print_list()
