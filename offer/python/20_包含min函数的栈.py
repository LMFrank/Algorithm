# -*- coding: utf-8 -*-
class Solution:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        # write code here
        min = self.min()
        if not min or node < min:
            self.minStack.append(node)
        else:
            self.minStack.append(min)
        self.stack.append(node)

    def pop(self):
        # write code here
        if self.stack:
            self.minStack.pop()
            return self.stack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]

    def min(self):
        # write code here
        if self.minStack:
            return self.minStack[-1]