from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, item):
        self.enqueue_stack.push(item)

    def dequeue(self):
        if self.dequeue_stack.is_empty():
            while not self.enqueue_stack.is_empty():
                self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()