# Challenge Title
Linked Lists implementation

## Whiteboard Process
N/A, I think

## Approach & Efficiency
Creation of a node class that represents the node in a linked list.

- Time Complexity

    - **Insert: O(1)** - insertion will always be a constant time per operation
    - **Includes: O(n)** - worst case is it'll need to go through the whole list
    - **to_string: O(n)** - it will need to go through each node one time

- Space Complexity

    - **Insert: O(1)** - No extra space needed, not dependant on linked list size
    - **Includes: O(1)** - No extra space needed, does not grow with input size
    - **to_string: O(n)** - String size will require more space as the number of nodes in the list increases

## Solution

- Happy Case: 

```
def test_return_all_values():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    assert linked_list.to_string() == "{ 2 } -> { 1 } -> NULL"
```

- Edge Case: Checks to the head of the empty list, points to newly inserted node

```
def test_edge_case_insert_into_empty_list():
    linked_list = LinkedList()
    linked_list.insert(1)
    assert linked_list.head is not None
    assert linked_list.head.value == 1
```

- Expected Failure: Calls an empty list but returns False

```
def test_expected_failure_search_in_empty_list():
    linked_list = LinkedList()
    assert not linked_list.includes(1)
```