# -*- coding: utf-8 -*-
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        pre = None
        temp = None
        while pHead:
            temp = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = temp
        return pre