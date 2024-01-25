class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class InvalidOperationError(Exception):
    pass

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError("Method not allowed on empty collection")
        dequeue_value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return dequeue_value

    def peek(self):
        if not self.front:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        return self.front is None
