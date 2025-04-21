# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Observation 1: This is a lightly modified BFS, so use a queue for traversal.
# Observation 2: When looping, check the size of the queue, which is how many nodes are in that level. 
# Observation 3: Once iterated over that many nodes, append that set to the solution list.

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if root is None:
            return []
        q.append(root)
        solution = []
        while len(q) > 0:
            level_size = len(q)
            level = []
            for i in range(0, level_size):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                level.append(node.val)
            solution.append(level)
        return solution
                
