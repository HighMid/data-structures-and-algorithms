from data_structures.binary_tree import BinaryTree, Node

def tree_intersection(tree_a, tree_b):

    def traverse_and_store(node, values_set):
        if node:
            values_set.add(node.value)
            traverse_and_store(node.left, values_set)
            traverse_and_store(node.right, values_set)
    
    values_set_a = set()
    traverse_and_store(tree_a.root, values_set_a)

    common_values = set()
    
    def collect_common_values(node, values_set, common_values):
        if node:
            if node.value in values_set:
                common_values.add(node.value)
            collect_common_values(node.left, values_set, common_values)
            collect_common_values(node.right, values_set, common_values)
    
    collect_common_values(tree_b.root, values_set_a, common_values)
    
    return list(common_values)
