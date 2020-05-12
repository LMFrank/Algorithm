class Node(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class SingleCircleLinkList(object):
    """循环单链表"""
    def __init__(self, node=None):
        self._head = node
        if node is not None:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        cur = self._head  # cur游标，用来遍历节点
        count = 1  # 记录数量
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return 0
        cur = self._head
        while cur.next != self._head:
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环时，cur指向尾结点，但尾结点元素未打印
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            self._head = node
            cur.next = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos < 0:
            self.add(item)
        elif pos >= (self.length() - 1):
            self.append(item)
        else:
            pre = self._head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self._head
        pre = None
        while cur.next != self._head:
            if cur.elem == item:
                # 先判断此节点是否是头结点
                if cur == self._head:
                    # 头结点，需要找尾节点
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self._head:
                # 链表只有一个节点
                self._head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """查找节点"""
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self._head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    li = SingleCircleLinkList()
    print(li.is_empty())
    print(li.length())

    li.append(1)
    print(li.is_empty())
    print(li.length())

    li.append(2)
    li.remove(2)
    print(li.is_empty())
'''
    li.add(6)
    for i in range(4, 8):
        li.append(i)
    li.travel()
    li.insert(-1, 9)
    li.travel()
    li.insert(2, 100)
    li.travel()
    li.insert(20, 200)
    li.travel()
    li.remove(9)
    li.travel()
    li.remove(200)
    li.travel()
    print(li.search(7))
    '''