from data_structures.binary_tree import BinaryTree, Node

class BinarySearchTree(BinaryTree):
    
    def add(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        def walk(node_to_ask, node_to_add):
            
            if node_to_add.value < node_to_ask.value:
                if node_to_ask.left is None:
                    node_to_ask.left = node_to_add
                else:
                    walk(node_to_ask.left, node_to_add)
                    
            elif node_to_add.value >= node_to_ask.value:
                if node_to_ask.right is None:
                    node_to_ask.right = node_to_add
                else:
                    walk(node_to_ask.right, node_to_add)

        walk(self.root, new_node)

    def contains(self, value):
        current = self.root
        while current:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
