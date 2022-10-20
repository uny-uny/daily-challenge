# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        pre=None
        max_count, curr_count, res = 0, 0, []
        if not root:
            return
        stack = []
        while True:
            while root:
                stack.append(root)            
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            curr_count = 1 if node.val != pre else curr_count + 1
            if curr_count == max_count:
                res.append(node.val)
            elif curr_count > max_count:
                res = [node.val]
                max_count = curr_count 
            pre = node.val
            root = node.right        