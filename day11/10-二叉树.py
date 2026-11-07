# 作者: 学不会
# 2026年10月16日19时15分33秒
# xxx@qq.com
import queue


class Node():
    def __init__(self, ele=-1, right=None, left=None):
        self.ele = ele
        self.right = right
        self.left = left


class Tree():
    def __init__(self):
        self.root = None
        self.queue = []  # 辅助队列

    def tree_build(self, value):
        new_node = Node(value)
        self.queue.append(new_node)  # 将新结点加入队列
        if self.root == None:
            self.root = new_node
        else:
            if self.queue[0].left == None:
                self.queue[0].left = new_node  # 新结点插入到左子树

            else:
                self.queue[0].right = new_node  # 新结点插入到右子树
                self.queue.pop(0)  # 弹出队列中第一个元素

    def pre_order(self, root):
        if root:
            print(root.ele, end=' ')
            self.pre_order(root.left)
            self.pre_order(root.right)

    def mid_order(self, root):
        if root:
            self.mid_order(root.left)
            print(root.ele, end=' ')
            self.mid_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.ele, end=' ')

    def level_order(self, root):
        self.queue.clear()
        self.queue.append(root)
        while self.queue:
            node: Node = self.queue.pop(0)
            print(node.ele, end=' ')
            if node.left:
                self.queue.append(node.left)
            if node.right:
                self.queue.append(node.right)


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 10):
        tree.tree_build(i)
    # 前序遍历
    tree.pre_order(tree.root)
    print()
    # 中序遍历
    tree.mid_order(tree.root)
    print()
    # 后序遍历
    tree.post_order(tree.root)
    print()
    # 层序遍历
    tree.level_order(tree.root)
    print()
