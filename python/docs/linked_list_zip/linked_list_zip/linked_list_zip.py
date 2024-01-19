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
    
    def kth_from_end(self, position):
        """
        Return the value of the node that is position positions from the end of the list.

        :param position: The position from the end (0-based).
        :return: The value at the kth position from the end.
        :raises TargetError: If position is out of range.
        """
        # First, count the number of nodes in the list
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        # Check if position is in a valid range
        if position < 0 or position >= count:
            raise TargetError("Position out of range")

        # Find the node (count - position - 1) steps from the start
        steps = count - position - 1
        current = self.head
        for _ in range(steps):
            current = current.next

        return current.value
    
    

def zip_lists(list_a, list_b):

        zipped = LinkedList()

        current_a = list_a.head
        current_b = list_b.head

        while current_a is not None or current_b is not None:
            if current_a:
                zipped.append(current_a.value)
                current_a = current_a.next

            if current_b:
                zipped.append(current_b.value)
                current_b = current_b.next

        return zipped    

class TargetError(Exception):
    pass
