# -*- coding: utf-8 -*-
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return None
        root.left, root.right = self.Mirror(root.right), self.Mirror(root.left)
        return root