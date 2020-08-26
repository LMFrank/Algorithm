# -*- coding: utf-8 -*-
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        else:
            return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1