# -*- coding: utf-8 -*-
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0))
        n = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre, tin[:n])
        root.right = self.reConstructBinaryTree(pre, tin[n+1:])
        return root