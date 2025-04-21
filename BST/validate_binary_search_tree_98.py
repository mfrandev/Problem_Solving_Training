# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Rule 1: Left subtree of a node contains only nodes with keys less than the node's key
# Rule 2: Right subtree of node contains only nodes with keys greater than the node's key
# Rule 3: Left and right subtrees must be BSTs.

# Observation 1: Trivally, "None" must be a valid BST. We are guaranteed to have at least one node though.
# Observation 2: Root value must be the "pivot" point for both the left and right subtrees. I.e., all nodes to the right of root must be larger, all nodes to the left must be smaller. 
# Observation 3: Passing the root key through the recursion should be sufficient to enforce the BST analysis. 

# Conversation 1: Observations 2 and 3 are flawed because we need to maintain a satisfiability range as we recurse through the tree. 
# Conversation 2: Moving left means no value may be larger than the current node's value.
# Conversation 3: Moving right means no value may be smaller than the current node's value. 
# Conversation 4: If at any point one of the previous two points are invalid, will return false.
# Conversation 5: Think of the solution to this problem as satifying a changing inequality. This is really simple to maintain and doesn't overcomplicate the problem. 

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def analyzeBST(node, minimum, maximum):
            if not node:
                return True
            
            print(f'{minimum}<{node.val}<{maximum}')
            if not (node.val < maximum and node.val > minimum):
                return False
            
            return analyzeBST(node.left, minimum, node.val) and analyzeBST(node.right, node.val, maximum)
        
        return analyzeBST(root, float("-inf"), float("inf"))
