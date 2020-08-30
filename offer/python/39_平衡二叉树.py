# -*- coding: utf-8 -*-
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        is_left = self.IsBalanced_Solution(pRoot.left)
        if not is_left:
            return False
        is_right = self.IsBalanced_Solution(pRoot.right)
        if not is_right:
            return False
        left_depth = pRoot.left.depth if pRoot.left else 0
        right_depth = pRoot.right.depth if pRoot.right else 0
        pRoot.depth = max(left_depth, right_depth) + 1
        return abs(left_depth - right_depth) <= 1

