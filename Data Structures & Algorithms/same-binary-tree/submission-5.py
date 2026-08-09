# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True

        stack = [(p, q)]
        while stack:
            x, y = stack.pop()
            
            if x and y and x.val == y.val:
                stack.append((x.left, y.left))
                stack.append((x.right, y.right))
            elif not x and not y:
                continue
            else:
                return False

        return True        
