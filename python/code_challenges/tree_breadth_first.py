from data_structures.binary_tree import BinaryTree
from collections import deque



def breadth_first(tree):
    
    if tree.root is None:
        return []
    
    queue = deque([tree.root])
    order = []
    
    while queue:
        current_node = queue.popleft()
        order.append(current_node.value)
        
        if current_node.left:
            queue.append(current_node.left)
            
        if current_node.right:
            queue.append(current_node.right)
            
    return order
