class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双链表"""
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """链表是否为空"""
        return self._head is None
    
    def length(self):
        """链表长度"""
        cur = self._head  # cur游标，用来遍历节点
        count = 0  # 记录数量
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self._head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self._head
        self._head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """
        指定位置添加元素
        :param pos 从0开始
        """
        if pos < 0:
            self.add(item)
        elif pos >=(self.length() - 1):
            self.append(item)
        else:
            cur = self._head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev = node
            node.prev.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        while cur is not None:
            if cur.elem == item:
                # 先判断此节点是否是头结点
                if cur == self._head:
                    self._head = cur.next
                    if cur.next is not None:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:        
                    cur.prev.next = cur.next
                    if cur.next is not None:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        """查找节点"""
        cur = self._head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    li = DoubleLinkList()
    print(li.is_empty())
    print(li.length())

    li.append(1)
    print(li.is_empty())
    print(li.length())

    li.append(2)
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
