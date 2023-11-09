class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        # Create the new node
        new_node = Node(data)
        # Check whether the linked list has a head node
        if self.head:
            # Point the next node of the new node to the head
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def remove_at_beginning(self):
        # The "next" node of the head becomes the new head node
        self.head = self.head.next

    def search(self, data):
        current_data = self.head
        while current_data:
            if current_data.value == data:
                return True
            else:
                current_data = current_data.next
        return False
