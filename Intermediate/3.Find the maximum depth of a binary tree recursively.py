# 3.Find the maximum depth of a binary tree recursively.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to find the maximum depth of a binary tree
def max_depth(root: TreeNode) -> int:
    # Base case: if the node is None, depth is 0
    if root is None:
        return 0

    # Recursively find the depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # Add 1 for the current node and return the maximum of the two depths
    return 1 + max(left_depth, right_depth)


# ---- Example Usage ----
if __name__ == "__main__":
    # Construct the binary tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n2 = TreeNode(2, n4, n5)
    n3 = TreeNode(3)
    root = TreeNode(1, n2, n3)

    # Find and print the maximum depth
    print("Maximum depth of the binary tree is:", max_depth(root))


# Output 

# Maximum depth of the binary tree is: 3