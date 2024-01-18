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
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, target, value):
        if not self.head:
            raise TargetError("List is empty")
        if self.head.value == target:
            self.insert(value)
            return
        current = self.head
        while current.next and current.next.value != target:
            current = current.next
        if current.next is None:
            raise TargetError(f"Target {target} not found")
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def insert_after(self, target, value):
        if not self.head:
            raise TargetError("List is empty")
        current = self.head
        while current and current.value != target:
            current = current.next
        if current is None:
            raise TargetError(f"Target {target} not found")
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(f"{{ {current.value} }}")
            current = current.next
        result.append("NULL")
        return " -> ".join(result)

class TargetError(Exception):
    pass
