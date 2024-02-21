import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection

def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)

def test_no_common_elements():
    tree_a = BinaryTree()
    add_values_to_empty_tree(tree_a, [1, 2, 3, 4, 5])

    tree_b = BinaryTree()
    add_values_to_empty_tree(tree_b, [6, 7, 8, 9, 10])

    assert tree_intersection(tree_a, tree_b) == []

def test_all_elements_common():
    tree_a = BinaryTree()
    add_values_to_empty_tree(tree_a, [11, 7, 15, 5, 9, 13, 17])

    tree_b = BinaryTree()
    add_values_to_empty_tree(tree_b, [11, 7, 15, 5, 9, 13, 17])

    assert sorted(tree_intersection(tree_a, tree_b)) == sorted([11, 7, 15, 5, 9, 13, 17])

def test_one_tree_empty():
    tree_a = BinaryTree()
    add_values_to_empty_tree(tree_a, [20, 10, 30, 5, 15, 25, 35])

    tree_b = BinaryTree()  # Empty tree

    assert tree_intersection(tree_a, tree_b) == []

def test_one_common_element():
    tree_a = BinaryTree()
    add_values_to_empty_tree(tree_a, [40, 20, 60, 10, 30, 50, 70])

    tree_b = BinaryTree()
    add_values_to_empty_tree(tree_b, [15, 5, 25, 35, 45, 55, 40])

    assert tree_intersection(tree_a, tree_b) == [40]

def test_common_elements_are_leaves():
    tree_a = BinaryTree()
    add_values_to_empty_tree(tree_a, [100, 50, 150, 25, 75, 125, 175])

    tree_b = BinaryTree()
    add_values_to_empty_tree(tree_b, [200, 100, 300, 50, 150, 250, 350])

    assert sorted(tree_intersection(tree_a, tree_b)) == sorted([100, 50, 150])
