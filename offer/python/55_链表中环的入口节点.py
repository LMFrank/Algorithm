# -*- coding: utf-8 -*-
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None or pHead.next == None or pHead.next.next == None:
            return None
        low = pHead.next
        fast = pHead.next.next

        while low != fast:
            if fast.next == None or fast.next.next == None:
                return None
            low = low.next
            fast = fast.next.next
        fast = pHead

        while low != fast:
            low = low.next
            fast = fast.next
        return fast