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
def test_right_join():
    legit = {
        "BASED": "Genuine",
        "Chill": "Calm",
    }
    hoax = {
        "BASED": "pretentious",
        "Chill": "Tense",
    }
    expected = [
        ["BASED", "pretentious", "Genuine"],
        ["Chill", "Tense", "Calm"],
    ]
    actual = left_join(legit, hoax, join='right')
    assert actual == expected
```
- Edge Case:

```
def test_empty_hash():
    nothing = {}
    
    actual = left_join(nothing, nothing)
    assert actual == []
```
- Expected Failure - If function has no AssertionError raised

```
def test_left_join_no_keys():
    empty1 = {}
    empty2 = {}
    with pytest.raises(AssertionError):
        assert left_join(empty1, empty2) != []
```