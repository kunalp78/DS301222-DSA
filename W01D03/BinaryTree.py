# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.data = data
#         self.right = None

# 3 kinds of traversal
# 1) inorder traversal - leftsubtree --> current Node --> right subtree
# 2) pre-order traversal - current Node --> left subtree --> right subtree
# 3) post-order traversal - left subtree --> right subtree --> current Node

class Node:
    def __init__(self, data):
        # self.root = None
        self.left = None
        self.data = data
        self.right = None
    
    def inorder_traversal(self):
        if self.left is not None:
            self.left.inorder_traversal()

        print(self.data)

        if self.right is not None:
            self.right.inorder_traversal()
    
    def preorder_traversal(self, current_node):
        if current_node is not None:
            print(current_node.data)
            self.preorder_traversal(current_node.left)
            self.preorder_traversal(current_node.right)

    def postorder_traversal(self, current_node):
        if current_node is not None:
            self.postorder_traversal(current_node.left)
            self.postorder_traversal(current_node.right)
            print(current_node.data)

root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("inodrder traversal:")
root.inorder_traversal()
print("preorder traversal:")
root.preorder_traversal(root)
print("postorder traversal:")
root.postorder_traversal(root)           