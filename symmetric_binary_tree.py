#use Depth First Search with both left and right nodes

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetrical(root):
    if root is None:
        return True
    
    def dfs(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.val == right.val and 
                dfs(left.left, right.right) and 
                dfs(left.right, right.left))
    
    return dfs(root.left, root.right)



def buildSymmetricalTree():
    # Building the following symmetrical binary tree
    #       1
    #      / \
    #     2   2
    #    / \ / \
    #   3  4 4  3
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, TreeNode(4), TreeNode(3))
    return root

def buildAsymmetricalTree():
    # Building the following asymmetrical binary tree
    #       1
    #      / \
    #     2   2
    #      \   \
    #      3    3
    root = TreeNode(1)
    root.left = TreeNode(2, None, TreeNode(3))
    root.right = TreeNode(2, None, TreeNode(3))
    return root

def printTree(root, level=0, label="."):
    if root is not None:
        print(" " * (level * 4) + label + ": " + str(root.val))
        printTree(root.left, level + 1, "L")
        printTree(root.right, level + 1, "R")

# Build symmetrical tree
symmetrical_root = buildSymmetricalTree()
print("Symmetrical Tree:")
printTree(symmetrical_root)
print("Is symmetrical:", isSymmetrical(symmetrical_root))

# Build asymmetrical tree
asymmetrical_root = buildAsymmetricalTree()
print("\nAsymmetrical Tree:")
printTree(asymmetrical_root)
print("Is symmetrical:", isSymmetrical(asymmetrical_root))
