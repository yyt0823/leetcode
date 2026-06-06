# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/
#
# Given the root of a binary tree and an integer targetSum, return the number
# of paths where the sum of the values along the path equals targetSum.
#
# The path does not need to start or end at the root or a leaf, but it must go
# downwards (traveling only from parent nodes to child nodes).
#
# Constraints:
#   - Number of nodes in [0, 1000]
#   - -10^9 <= Node.val <= 10^9
#   - -1000 <= targetSum <= 1000

from collections import deque
from typing import Optional


class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def pathSum(self, root: Optional[Node], targetSum: int) -> int:
        count = 0
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            if not cur:
                continue
            q.append(cur.left)
            q.append(cur.right) 
            count += self.count_from(cur, targetSum)
        return count
            
            
    
    def count_from(self,node:Node, remaining:int) -> int:
        if not node:
            return 0
        count = 0
        if node.val == remaining:
            count += 1
        count += self.count_from(node.left, remaining - node.val)
        count += self.count_from(node.right, remaining - node.val)
        return count
            
            
    
    

def build(values: list[Optional[int]]) -> Optional[Node]:
    if not values:
        return None
    values = deque(values)
    arr = deque()
    root = Node(values.popleft())
    arr.append(root)
    while arr and values:
        cur = arr.popleft()
        if not cur:
            continue
        left = values.popleft()
        right = values.popleft()
        if left is not None:
            cur.left = Node(left)
            arr.append(cur.left)
        if right is not None:
            cur.right = Node(right)
            arr.append(cur.right)
    return root
        
        
    
    
    
    
if __name__ == "__main__":
    t1 = build([10,5,-3,3,2,None,11,3,-2,None,1])
    assert Solution().pathSum(t1,8) == 3
    print("all test passed")



        
