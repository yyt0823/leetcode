# 1372. Longest ZigZag Path in a Binary Tree
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
#
# You are given a root of a binary tree. A ZigZag path is defined as:
#   - Choose any node and a direction (right or left).
#   - If the current direction is right, move to the right child; otherwise left.
#   - Flip the direction.
#   - Repeat until you can't move.
#
# The zigzag length is the number of edges traversed.
# Return the longest ZigZag path in the tree.
#
# Constraints:
#   - Number of nodes in [1, 50000]
#   - 1 <= Node.val <= 100

from typing import Optional
from collections import deque

class Direction:
    LEFT = "left"
    RIGHT = "right"

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_count = 0
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            if not cur:
                continue
            left = cur.left
            right = cur.right
            if left is not None:
                q.append(left)
            if right is not None:
                q.append(right)
            max_local =  max(self.zigZag(cur,"left"), self.zigZag(cur,"right"))
            max_count = max(max_count, max_local)
        return max_count
            
            
         
                
        
       
    def zigZag(self, node: TreeNode, direction: Direction):
        if not node:
            return 0
        count = 0
        if direction == "left":
            if node.left is None:
                return 0 
            count += self.zigZag(node.left, "right") + 1
        else: 
            if node.right is None:  
                return 0 
            count += self.zigZag(node.right, "left") + 1
            
        return count
        
class Solution2:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.aug_dfs(root, 0, 0)
        return self.result

    def aug_dfs(self, root: Optional[TreeNode], left: int, right: int):
        if not root:
            return
        self.result = max(self.result, left, right)
        if root.left is not None:
            self.aug_dfs(root.left, right + 1, 0)
        if root.right is not None:
            self.aug_dfs(root.right, 0, left + 1)
        
            
        

        
    
        

def build(values: list[Optional[int]]) -> TreeNode:
    if not values:
        return None
    values = deque(values)
    root = TreeNode(values.popleft())
    q = deque()
    q.append(root)

    while q and values:
        cur = q.popleft()
        left = values.popleft() if values else None
        right = values.popleft() if values else None

        if left is not None:
            cur.left = TreeNode(left)
            q.append(cur.left)
        if right is not None:
            cur.right = TreeNode(right)
            q.append(cur.right)
    return root
    


if __name__ == "__main__":
    t1 = build([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
    assert Solution2().longestZigZag(t1) == 3
    t2 = build([1,1,1,None,1,None,None,1,1,None,1])
    assert Solution2().longestZigZag(t2) == 4
    
    
    
    