#Depth First Search allow to solve recursively.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root is None:
        return None
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    # Recursively invert the left and right subtrees
    invertTree(root.left)
    invertTree(root.right)
    return root

# Helper Functions ti display the tree

def printTree(root, level=0, label="."):
    if root is not None:
        print(" " * (level * 4) + label + ": " + str(root.val))
        printTree(root.left, level + 1, "L")
        printTree(root.right, level + 1, "R")

def buildExampleTree():
    # Building the following binary tree
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    # In the original tree, the left subtree of the root node is (2, 4, 5) and 
    # the right subtree is (3, 6). After inverting, the left subtree becomes (3, 6) and 
    # the right subtree becomes (2, 5, 4), effectively swapping the left and right children at each node.
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))
    return root


# Build the example tree
root = buildExampleTree()
print("Original Tree:")
printTree(root)

# Invert the tree
invertTree(root)
print("\nInverted Tree:")
printTree(root)
