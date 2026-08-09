# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        queue = deque([(root, float('-inf'), float('inf'))])
        while queue:
            node, minimum, maximum = queue.popleft()
            if node.val <= minimum or node.val >= maximum:
                return False
            if node.left:
                queue.append((node.left, minimum, node.val))
            if node.right:
                queue.append((node.right, node.val, maximum))
        
        return True    
        