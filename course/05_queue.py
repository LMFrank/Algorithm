class Queue(object):
    """队列"""

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列添加一个元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列大小"""
        return len(self.__list)

if __name__ == '__main__':
    q = Queue()
    for i in range(4):
        q.enqueue(i)

    for i in range(4):
        print(q.dequeue())