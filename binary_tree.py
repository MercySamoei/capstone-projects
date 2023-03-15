class Binary_tree:

    def __init__(self, insert):
        self.left_node = None
        self.right_node = None
        self.insert = insert

    def insert_(self, number):
        if number > self.insert:
            if self.right_node is None:
                self.right_node = Binary_tree(number)
                print(f"Number {number} has been inserted to the right child of {self.insert}")
            else:
                self.right_node.insert_(number)
        elif number < self.insert:
            if self.left_node is None:
                self.left_node = Binary_tree(number)
                print(f"Number {number} has been inserted to the left child of {self.insert}")
            else:
                self.left_node.insert_(number)

    def promote_child(self, child_node):
        self.insert = child_node.insert
        self.left_node = child_node.left_node
        self.right_node = child_node.right_node

    def __str__(self):
        left_number = self.left_node.insert if self.left_node is not None else "None"
        right_number = self.right_node.insert if self.right_node is not None else "None"
        return (f"Parent Node:{self.insert} Child nodes({left_number}, {right_number})")
    
tree = Binary_tree(8)
tree.insert_(5)
tree.insert_(15)
tree.insert_(3)
tree.insert_(7)
tree.insert_(12)
tree.insert_(20)

print(tree)








    
