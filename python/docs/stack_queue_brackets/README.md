# Challenge Title
stack_queue_brackets

## Whiteboard Process
N/A

## Approach & Efficiency
Create an empty stack for the brackets, looping through each character in the string and checking open brackets to push to the stack.

- Time Complexity

    - **bracket_validation O(n)** - worst case, this iterates through each character and increases via input size


- Space Complexity

    - **bracket_validation O(n)** - worst case, if all characters are open brackets, will have to be pushed to the stack. **O(1)** if the input is perfect already or has no brackets.

## Solution

- Happy Case: 

```
def test_balanced_brackets():
    input_string = "{}(){}"
    assert multi_bracket_validation(input_string) == True
```

- Edge Case: Checks to see if queue/dequeue and push/pop works correctly

```
def test_empty_string():
    input_string = ""
    assert multi_bracket_validation(input_string) == True
```

- Expected Failure: Popping or peeking from an empty stack/queue raising an Error

```
def test_unbalanced_brackets():
    input_string = "{(})"
    assert multi_bracket_validation(input_string) == False
```