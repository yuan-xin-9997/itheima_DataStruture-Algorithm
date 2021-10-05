# -*- coding: utf-8 -*-
"""
@author: yuan_xin
@contact: yuanxin9997@qq.com
@file: 3-1_single_link_list.py
@time: 2020/10/20 9:56
@description:用Python实现单向链表
"""


class SingleNode(object):
    """单链表的结点"""
    def __init__(self, item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None


class SingleLinkList(object):
    """单链表实现（单链表的操作）：
        is_empty() 链表是否为空
        length() 链表长度
        travel() 遍历整个链表
        add(item) 链表头部添加元素
        append(item) 链表尾部添加元素
        insert(pos, item) 指定位置添加元素
        remove(item) 删除节点
        search(item) 查找节点是否存在
    """
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self.__head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur is not None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.item, end=',')
            cur = cur.next
        print()

    def add(self, item):
        """头部添加元素，头插法"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self.__head
        # 将链表的头_head指向新节点
        self.__head = node

    def append(self, item):
        """尾部添加元素，尾插法"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将__head指向新节点
        if self.is_empty():
            self.__head = node
        # 若不为空，则找到尾部，将尾结点的next指向新节点
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos < 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        # 找到指定位置
        else:
            # 先创建一个保存item值的节点
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.__head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur is not None:
            # 如果找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self.__head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False


# 测试单向链表
if __name__ == "__main__":
    # 创建单向链表
    ll = SingleLinkList()
    # 添加元素
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print('length:', ll.length())
    # 遍历
    ll.travel()
    # 查找元素
    print(ll.search(3))
    print(ll.search(5))
    # 删除元素
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()
