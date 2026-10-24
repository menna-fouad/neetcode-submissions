# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot or not root:
            return False

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val and self.checkSubTree(node, subRoot):
                    return True
            
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        
        return False
        
    def checkSubTree(self, root, subRoot):
        stack = [(root, subRoot)]
        while stack:
            main, sub = stack.pop()
            if not main and not sub:
                continue
                
            if not main or not sub or main.val != sub.val:
                return False
                
            stack.append((main.left, sub.left))
            stack.append((main.right, sub.right))
            
        return True
        