# 作者: 学不会
# 2026年10月24日11时10分50秒
# xxx@qq.com

RED = 0
BLACK = 1


class RedBlackNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.p = None
        self.color = RED


class RedBlackTree:
    def __init__(self):
        self.root = None

    # 左旋
    def left_child(self, x: RedBlackNode):
        y: RedBlackNode = x.right
        x_parent = x.p
        if x_parent is None:  # 说明x是根节点
            self.root = y
        elif x_parent.left is x:
            x_parent.left = y
        else:
            x_parent.right = y
        y.p = x_parent
        if y.left:  # 处理y的左子树
            y.left.p = x
        x.right = y.left
        y.left = x
        x.p = y

    # 右旋
    def right_child(self, x: RedBlackNode):
        y: RedBlackNode = x.left
        x_parent = x.p
        if x_parent is None:  # 说明x是根节点
            self.root = y
        elif x_parent.right is x:
            x_parent.right = y
        else:
            x_parent.left = y
        y.p = x_parent
        if y.right:
            y.right.p = x
        x.left = y.right
        y.right = x
        x.p = y

    # 插入节点
    def insert_node(self, value):
        new_node = RedBlackNode(value)
        if self.root is None:
            self.root = new_node
        else:
            x = self.root
            parent = None
            while x:
                parent = x
                if new_node.value < x.value:
                    x = x.left
                else:
                    x = x.right

            if new_node.value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.p = parent

        self.insert_fixup(new_node)

    def insert_fixup(self, x: RedBlackNode):
        parent = x.p
        while parent and parent.color == RED:
            gparent: RedBlackNode = parent.p
            if gparent.left is parent:  # 父节点是左孩子
                uncle = gparent.right
                # 情3
                if uncle and uncle.color == RED:  # 父节点的叔叔是红色,叔父爷染色，爷变为新结点
                    gparent.color = RED
                    uncle.color = BLACK
                    parent.color = BLACK
                    x = gparent  # 爷爷变成新结点，继续向上调整
                    parent = x.p
                    continue
                # 情4,左旋之后一定是情5
                if parent.right is x:  # 叔叔是黑色
                    # 父节点是左孩子，且新结点是右孩子，LR型：左、右双旋，儿换爷+染色
                    self.left_child(parent)
                # 情5
                self.right_child(gparent)
                parent.color = BLACK
                gparent.color = RED
            else:  # 对称的情况
                uncle = gparent.left
                # 情3
                if uncle and uncle.color == RED:  # 父节点的叔叔是红色,叔父爷染色，爷变为新结点
                    gparent.color = RED
                    uncle.color = BLACK
                    parent.color = BLACK
                    x = gparent  # 爷爷变成新结点，继续向上调整
                    parent = x.p
                    continue
                # 情4,左旋之后一定是情5
                if parent.left is x:  # 叔叔是黑色
                    # 父节点是左孩子，且新结点是右孩子，LR型：左、右双旋，儿换爷+染色
                    self.right_child(parent)
                # 情5
                self.left_child(gparent)
                gparent.color = RED
                parent.color = BLACK


        self.root.color = BLACK

    def rbtree_print(self, node, key, direction):
        if node:
            if direction == 0:  # tree是根节点
                print("%2d(B) is root" % node.value)

            else:  # tree是分支节点
                print("%2d(%s) is %2d's %6s child" % (
                    node.value, ("B" if node.color == 1 else "R"), key,
                    ("right" if direction == 1 else "left")))

            self.rbtree_print(node.left, node.value, -1)
            self.rbtree_print(node.right, node.value, 1)


if __name__ == '__main__':
    number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    tree = RedBlackTree()

    for number in number_list:
        tree.insert_node(number)

    tree.rbtree_print(tree.root, 0, 0)
