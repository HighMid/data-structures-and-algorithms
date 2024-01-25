# Challenge Title
stack and queue

## Whiteboard Process
N/A

## Approach & Efficiency
Creation of Queue and Stack, this is implemented using a linked list.

- Time Complexity

    - **Stack: O(1)** - insertion/remove will always be a constant time per operation
    - **Queue: O(1)** - insertion/remove will always be a constant time per operation


- Space Complexity

    - **Stack: O(n)** - The space required grows linearly as more nodes gets added
    - **Queue: O(n)** - The space required grows linearly as more nodes gets added

## Solution

- Happy Case: 

```
def test_stack_operations():
    s = Stack()
    s.push("apple")
    s.push("banana")
    assert s.peek() == "banana"
    assert s.pop() == "banana"
    assert s.peek() == "apple"
    assert not s.is_empty()

def test_queue_operations():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    assert q.peek() == "apple"
    assert q.dequeue() == "apple"
    assert q.peek() == "banana"
    assert not q.is_empty()

```

- Edge Case: Checks to see if queue/dequeue and push/pop works correctly

```
def test_empty_after_operations():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.pop()
    s.pop()
    assert s.is_empty()

def test_empty_after_operations():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.dequeue()
    q.dequeue()
    assert q.is_empty()


```

- Expected Failure: Popping or peeking from an empty stack/queue raising an Error

```
def test_dequeue_from_empty_queue():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.dequeue()

def test_peek_from_empty_queue():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.peek()

def test_pop_from_empty_stack():
    s = Stack()
    with pytest.raises(InvalidOperationError):
        s.pop()

def test_peek_from_empty_stack():
    s = Stack()
    with pytest.raises(InvalidOperationError):
        s.peek()


```