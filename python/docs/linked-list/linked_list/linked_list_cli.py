class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class EmptyListError(Exception):
    """Exception raised when an operation is performed on an empty list."""
    pass

class LinkedList:
    def __init__(self):
        self.head = None
        
    def get_first(self):
        if self.head is None:
            raise EmptyListError("Cannot fetch from an empty list.")
        return self.head.value

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        values = []
        current = self.head
        while current:
            values.append(f"{{ {current.value} }}")
            current = current.next
        values.append("NULL")
        return " -> ".join(values)

# Example Usage
linked_list = LinkedList()
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(1)

print(linked_list.to_string())  # { 1 } -> { 2 } -> { 3 } -> NULL
print(linked_list.includes(2))  # True
print(linked_list.includes(4))  # False
