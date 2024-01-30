import pytest
from data_structures.binary_tree import BinaryTree, Node



def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

def test_empty_input():
    tree = BinaryTree()
    assert tree.find_maximum_value() is None
    
def test_negative_values():
    tree = BinaryTree()
    tree.root = Node(-5)
    tree.root.left = Node(-1)
    tree.root.right = Node(-22)
    
    actual = tree.find_maximum_value()
    expected = -1
    
    assert actual == expected
