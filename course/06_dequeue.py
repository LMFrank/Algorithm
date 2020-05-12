#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Dequeue(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        self.__list.insert(0, item)

    def add_rear(self, item):
        self.__list.append(item)

    def remove_front(self):
        self.__list.pop(0)

    def remove_rear(self):
        self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)
