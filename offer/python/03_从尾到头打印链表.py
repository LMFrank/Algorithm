# -*- coding: utf-8 -*-
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        p = listNode
        stack = []
        result = []
        while p:
            stack.append(p.val)
            p = p.next
        while stack:
            result.append(stack.pop())
        return result