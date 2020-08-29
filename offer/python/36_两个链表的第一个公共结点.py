# -*- coding: utf-8 -*-
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            if p1 == None:
                p1 = pHead2
            else:
                p1 = p1.next
            if p2 == None:
                p2 = pHead1
            else:
                p2 = p2.next
        return p2