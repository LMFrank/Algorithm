class Stack(object):
    """栈"""

    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新元素到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)

if __name__ == '__main__':
    s = Stack()
    for i in range(4):
        s.push(i)

    for i in range(4):
        print(s.pop())
