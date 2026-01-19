class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at(self, prev_data, data):
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if not current:
            return None
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        return data

    def remove_beginning(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def remove_at_end(self):
        if not self.head:
            return None
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            return removed_data
        current = self.head
        while current.next.next:
            current = current.next
        removed_data = current.next.data
        current.next = None
        return removed_data

    def remove_at(self, data):
        if not self.head:
            return None
        if self.head.data == data:
            return self.remove_beginning()
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if not current.next:
            return None
        removed_data = current.next.data
        current.next = current.next.next
        return removed_data

    def clear_list(self):
        self.head = None

    def search(self, data):
        current = self.head
        position = 1
        while current:
            if str(current.data) == str(data):
                return position
            current = current.next
            position += 1
        return None

    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) + " -> None" if nodes else "List is empty."

