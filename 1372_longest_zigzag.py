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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        pass


def build(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    values = deque(values)
    root = TreeNode(values.popleft())
    arr = deque([root])
    while arr and values:
        cur = arr.popleft()
        left = values.popleft() if values else None
        right = values.popleft() if values else None
        if left is not None:
            cur.left = TreeNode(left)
            arr.append(cur.left)
        if right is not None:
            cur.right = TreeNode(right)
            arr.append(cur.right)
    return root


if __name__ == "__main__":
    sol = Solution()

    t1 = build([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1])
    assert sol.longestZigZag(t1) == 3, "example 1 failed"

    t2 = build([1, 1, 1, None, 1, None, None, 1, 1, None, 1])
    assert sol.longestZigZag(t2) == 4, "example 2 failed"

    t3 = build([1])
    assert sol.longestZigZag(t3) == 0, "example 3 failed"

    print("all tests passed")
