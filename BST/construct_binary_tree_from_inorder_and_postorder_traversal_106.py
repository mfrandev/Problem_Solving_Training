# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Observation 1: The leftmost element of the array is guaranteed to be leftmost "leaf" node
# Observation 2: The last element of the in-order traversal is the rightmost leaf node
# Observation 3: the last element of the post-order traversal is the root node
# Observation 4: Everything to the left of the last element in post-order is below it. 
# Observation 5: Everything to the left of the root in in-order is to the left, while everything to the right is to the right.
# Observation 6: From right to left in post order traversal: Root, Right subtree, left subtree.
# Observation 7: When building right-to-left popping the post-order list gives the next root



class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 1:
            postorder.pop()
            return TreeNode(inorder[0])
        if len(inorder) == 0:
            return None
        root_index = inorder.index(postorder[-1])
        lhs, rhs = inorder[:root_index], inorder[root_index+1:]
        postorder.pop()
        right = self.buildTree(rhs, postorder)
        left = self.buildTree(lhs, postorder)
        return TreeNode(inorder[root_index], left, right)
