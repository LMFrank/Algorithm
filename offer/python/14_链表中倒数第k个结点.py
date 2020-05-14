# -*- coding: utf-8 -*-
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k < 0:
            return None
        p = q = head
        t = 0
        while p and t < k:
            p = p.next
            t += 1
        if t < k:
            return None
        while p:
            p = p.next
            q = q.next
        return q