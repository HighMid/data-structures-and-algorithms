from data_structures.queue import Queue


def multi_bracket_validation(input_str):
    bracket_pairs = {'[': ']', '{': '}', '(': ')'}
    open_brackets = set(bracket_pairs.keys())
    close_brackets = set(bracket_pairs.values())

    stack = []

    for char in input_str:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack:
                return False
            last_open = stack.pop()
            if bracket_pairs[last_open] != char:
                return False

    return len(stack) == 0
