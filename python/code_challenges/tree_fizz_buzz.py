from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(tree):
    
    if tree.root is None:
        return []
    
    
    def fizz_walk(node):
        
        if node.value % 15 == 0:
            value = "FizzBuzz"
        elif node.value % 3 == 0:
            value = "Fizz"
        elif node.value % 5 == 0:
            value = "Buzz"
        else:
            value = str(node.value)
        
        new_node = Node(value)

        for child in node.children:
            new_node.children.append(fizz_walk(child))
            
        return new_node
    
    new_tree = KaryTree(fizz_walk(tree.root))
    return new_tree
