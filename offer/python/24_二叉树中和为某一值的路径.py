# -*- coding: utf-8 -*-
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []

        result = []

        def FindPathMain(root, path, currentSum):
            currentSum += root.val

            path.append(root)
            isLeaf = root.left == None and root.right == None

            if currentSum == expectNumber and isLeaf:
                onePath = []
                for node in path:
                    onePath.append(node.val)
                result.append(onePath)

            if currentSum < expectNumber:
                if root.left:
                    FindPathMain(root.left, path, currentSum)
                if root.right:
                    FindPathMain(root.right, path, currentSum)

            path.pop()

        FindPathMain(root, [], 0)

        return result